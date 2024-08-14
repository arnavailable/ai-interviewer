from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
from tempfile import gettempdir

load_dotenv()


def synthesize_speech(text):
    client = OpenAI()
    response = client.audio.speech.create(model="tts-1",voice="echo",input=text)
    output = os.path.join(gettempdir(), "speech.mp3")
    response.stream_to_file(output)

    # Play the audio using the platform's default player
    st.audio(output, format="audio/mp3", autoplay=True)

    return output