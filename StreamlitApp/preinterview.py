import streamlit as st
import logging
import logging.handlers
import queue
import threading
import time
import os
from collections import deque
from pathlib import Path
from typing import List
import av
import numpy as np
import pydub
import streamlit as st
from twilio.rest import Client
from dotenv import load_dotenv
from streamlit_webrtc import WebRtcMode, webrtc_streamer
from speech_recognition.openai_whisper import transcribe

load_dotenv()

HERE = Path(__file__).parent

logger = logging.getLogger(__name__)

# This code is based on https://github.com/whitphx/streamlit-webrtc/blob/c1fe3c783c9e8042ce0c95d789e833233fd82e74/sample_utils/turn.py
@st.cache_data  # type: ignore
def get_ice_servers():
    """Use Twilio's TURN server because Streamlit Community Cloud has changed
    its infrastructure and WebRTC connection cannot be established without TURN server now.  # noqa: E501
    We considered Open Relay Project (https://www.metered.ca/tools/openrelay/) too,
    but it is not stable and hardly works as some people reported like https://github.com/aiortc/aiortc/issues/832#issuecomment-1482420656  # noqa: E501
    See https://github.com/whitphx/streamlit-webrtc/issues/1213
    """

    # Ref: https://www.twilio.com/docs/stun-turn/api
    try:
        account_sid = "AC4fdeb5f79758bbf98082092848d69d96"
        auth_token = "79efa3dad3b5af5a4b97fe727b6d70c6"
    except KeyError:
        logger.warning(
            "Twilio credentials are not set. Fallback to a free STUN server from Google."  # noqa: E501
        )
        return [{"urls": ["stun:stun.l.google.com:19302"]}]

    client = Client(account_sid, auth_token)

    token = client.tokens.create()

    return token.ice_servers

def main():
    st.header("Real Time Speech-to-Text")
    app_sst_with_video()

def app_sst_with_video():
    frames_deque_lock = threading.Lock()
    frames_deque: deque = deque([])

    async def queued_audio_frames_callback(
        frames: List[av.AudioFrame],
    ) -> av.AudioFrame:
        with frames_deque_lock:
            frames_deque.extend(frames)

        # Return empty frames to be silent.
        new_frames = []
        for frame in frames:
            input_array = frame.to_ndarray()
            new_frame = av.AudioFrame.from_ndarray(
                np.zeros(input_array.shape, dtype=input_array.dtype),
                layout=frame.layout.name,
            )
            new_frame.sample_rate = frame.sample_rate
            new_frames.append(new_frame)

        return new_frames

    webrtc_ctx = webrtc_streamer(
        key="speech-to-text-w-video",
        mode=WebRtcMode.SENDRECV,
        queued_audio_frames_callback=queued_audio_frames_callback,
        rtc_configuration={"iceServers": get_ice_servers()},
        media_stream_constraints={"video": True, "audio": True},
    )

    status_indicator = st.empty()

    if not webrtc_ctx.state.playing:
        return

    status_indicator.write("Loading...")
    text_output = st.empty()
    text = ""

    # if not stop_button:
    while True:
        if webrtc_ctx.state.playing:

            sound_chunk = pydub.AudioSegment.empty()
            audio_frames = []
            window = 2000
            window_start = 0
            window_end = window

            # Get the audio frames that have arrived
            with frames_deque_lock:
                while len(frames_deque) > 0:
                    frame = frames_deque.popleft()
                    audio_frames.append(frame)

            # If no audio frames have arrived, wait for 100ms
            if len(audio_frames) == 0:
                time.sleep(0.1)
                status_indicator.write("No frame arrived.")
                continue

            # If audio frames have arrived, update the status indicator
            status_indicator.write("Running. Say something!")

            # Create an audio chunk from the audio frames that have arrived based on window size
            while (len(sound_chunk) >= window_start) and (len(sound_chunk) < window_end):
                for audio_frame in audio_frames:
                    sound = pydub.AudioSegment(
                        data=audio_frame.to_ndarray().tobytes(),
                        sample_width=audio_frame.format.bytes,
                        frame_rate=audio_frame.sample_rate,
                        channels=len(audio_frame.layout.channels),
                    )
                    sound_chunk += sound
                
            # Select the audio chunk to transcribe based on the window size, add a 10ms cushion

            chunk = sound_chunk[window_start:window_end]
            # chunk = sound_chunk

            # Save the audio chunk to a .wav file
            chunk.export("temp/audio.wav", format="wav")
                
            # Transcribe the audio using a speech-to-text function
            transcription = transcribe("temp/audio.wav")

            # Append the transcription to the text
            text += transcription

            # text = transcribe("temp/audio.wav")

            # Display the text
            text_output.markdown(f"**Text:** {text}")

            # Update the window start and end
            window_start += window
            window_end += window

        else:
            status_indicator.write("Stopped.")
            break

if __name__ == "__main__":
    import os

    DEBUG = os.environ.get("DEBUG", "false").lower() not in ["false", "no", "0"]

    logging.basicConfig(
        format="[%(asctime)s] %(levelname)7s from %(name)s in %(pathname)s:%(lineno)d: "
        "%(message)s",
        force=True,
    )

    logger.setLevel(level=logging.DEBUG if DEBUG else logging.INFO)

    st_webrtc_logger = logging.getLogger("streamlit_webrtc")
    st_webrtc_logger.setLevel(logging.DEBUG)

    fsevents_logger = logging.getLogger("fsevents")
    fsevents_logger.setLevel(logging.WARNING)

    main()