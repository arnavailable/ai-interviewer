import streamlit as st
import cv2
import threading
import speech_recognition as sr
import pyaudio
import wave
import time
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Define global variables
stop_event = None

# Function to record audio
def record_audio(filename="output_audio.wav", sample_rate=44100, chunk=4096, channels=1):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk)
    frames = []

    while not stop_event.is_set():
        data = stream.read(chunk, exception_on_overflow=False)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

# Function to transcribe audio
def transcribe_audio(filename="output_audio.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from speech recognition service; {e}"

# Function to handle video capture
def capture_video(video_filename="output_video.avi"):
    cap = cv2.VideoCapture(0)
    # Get video properties
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_filename, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
    
    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            break
        # Write the frame into the file
        out.write(frame)
    
    cap.release()
    out.release()

# Main execution in Streamlit
st.title("Video Recording with Audio Transcription")

# Record and capture buttons
if st.button("Start Recording"):
    stop_event = threading.Event()  # Initialize stop_event here
    
    # Start audio recording in a separate thread
    audio_thread = threading.Thread(target=record_audio)
    audio_thread.start()

    # Start video recording
    capture_video()  # Start capturing video

    audio_thread.join()  # Wait for the audio recording to finish

    st.success("Recording finished!")

    # Transcribe the audio
    transcription = transcribe_audio()
    st.write("Transcription:")
    st.write(transcription)

    # Display the recorded video
    st.video("output_video.avi")

if st.button("Stop Recording"):
    if stop_event is not None:
        stop_event.set()

# Clean up old files
if os.path.exists("output_audio.wav"):
    os.remove("output_audio.wav")
if os.path.exists("output_video.avi"):
    os.remove("output_video.avi")






