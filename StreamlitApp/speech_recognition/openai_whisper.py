from openai import OpenAI
import assemblyai as aai
import os
from dotenv import load_dotenv
load_dotenv()
import wave

OpenAI.api_key = os.getenv("OPENAI_API_KEY")
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

class Config:
    channels = 2
    sample_width = 2
    sample_rate = 44100

def save_wav_file(file_path, wav_bytes):
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(Config.channels)
        wav_file.setsampwidth(Config.sample_width)
        wav_file.setframerate(Config.sample_rate)
        wav_file.writeframes(wav_bytes)

def transcribe(file_path):
    # client = OpenAI()
    # audio_file= open(file_path, "rb")
    # transcription = client.audio.transcriptions.create(
    # model="whisper-1", 
    # file=audio_file
    # )

    transcriber = aai.Transcriber()
    transcription = transcriber.transcribe(file_path)

    return transcription.text

# print(transcribe("audio.wav"))


