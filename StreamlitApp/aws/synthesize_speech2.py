import streamlit as st
import os
from tempfile import gettempdir
from gtts import gTTS

def synthesize_speech(text):
    tts = gTTS(text=text, lang='en')
    output = os.path.join(gettempdir(), "speech.mp3")
    tts.save(output)

    # Play the audio using the platform's default player
    st.audio(output, format="audio/mp3", autoplay=True)

    return output