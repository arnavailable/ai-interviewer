#########################################################################################
## Keys and Tokens

OPENAI_API_KEY = "sk-1W6914esN5qg0ZwDySKMdxcf2LkDr-gPym4CpTATv1T3BlbkFJw05DMfogYmZGuHrMqc1dPJV1CbZPZQ_J8AlrX2oxMA"
ANTHROPIC_API_KEY = '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'
GOOGLE_API_KEY = 'AIzaSyBsBhlVsf9OJl1-4_yofzk8bdziDagIZao'
#########################################################################################
## Import Libraries

import streamlit as st
from streamlit_lottie import st_lottie
from typing import Literal
from dataclasses import dataclass
import json
import base64
from langchain.memory import ConversationBufferMemory
from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain, RetrievalQA
from langchain.prompts.prompt import PromptTemplate
from langchain.text_splitter import NLTKTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import nltk
from prompts.prompts import templates
import anthropic

# Import Audio Libraries
from speech_recognition.openai_whisper import save_wav_file, transcribe
from audio_recorder_streamlit import audio_recorder
from aws.synthesize_speech import synthesize_speech
from IPython.display import Audio
import speech_recognition as sr

# Import Video Libraries
import logging
import logging.handlers
import queue
import threading
import time
import urllib.request
import os
from collections import deque
from pathlib import Path
from typing import List

# Import Audio Libraries
import av
import numpy as np
import pydub
import streamlit as st
from twilio.rest import Client

# Import Streamlit WebRTC
from streamlit_webrtc import WebRtcMode, webrtc_streamer
#########################################################################################
## Questions for MVP

questions = [ 
             # Instructions
             "I am going to ask you a few questions to better understand your background and experience. \
             Please answer honestly and to the best of your ability. \
             There are no right or wrong answers, we are just trying to get to know you better. \
             When your answer has ended, please say the statement 'My answer has ended'. \
             Are you ready to begin?",

             # Pleasantries
             "Hi! How are you doing today?", 
             "What is your name?", 

             # Qualifying the candidate
             "What is your expected annual salary range for this role?", 
             "What is your current work or employment authorisation?",
             "Are you able to work on-site 3 days a week?",

             # Custom Questions for Job Description: Customized by the Account Manager
             "What is your ICP",
             "Base salary for this role is fixed at $70000, will that work for you? If not, would you withdraw your application for this role?",
             "Do you have experience with technical-SaaS based companies?",

             # Technical Interview
             "What is your experience in audio processing?",
             "What is your experience in image processing?",
             "What is your experience in data analysis?",
             "What is your experience in data visualization?"
             ]
#########################################################################################
## Define Functions

# Function to load a Lottie file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
# 

# Function to transcribe speech from an audio file (.wav)
import speech_recognition as sr
def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from speech recognition service; {e}"

# Function to switch LLM models
def llm_model(llm):
    if llm == "chatgpt":
        return ChatOpenAI(
            openai_api_key = OPENAI_API_KEY,
            model_name="gpt-3.5-turbo",
            temperature=0.8, )
    elif llm == "anthropic":
        return anthropic.Anthropic(
            api_key=ANTHROPIC_API_KEY,
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0, )

# Function to maintain chatbot history

# Function to generate a chatbot response

# Function to start video recording

# Function to generate an audio response using text-to-speech
from gtts import gTTS
def text_to_speech(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    return "response.mp3"

# 
#########################################################################################
## Main Webpage Layout

# Set Page Title
st_lottie(load_lottiefile("images/welcome.json"), speed=1, reverse=False, loop=True, quality="high", height=300)