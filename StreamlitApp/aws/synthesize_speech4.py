import streamlit as st
import os
from dotenv import load_dotenv
from tempfile import gettempdir
import boto3
from contextlib import closing
import sys

load_dotenv()

Session = boto3.Session(
        aws_access_key_id = "AKIA5FTZCRWWE7V4QPG2",
        aws_secret_access_key = "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",
        region_name = "us-east-1"
    )

def synthesize_speech(text):
    Polly = Session.client("polly")
    response = Polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Joanna")
    if "AudioStream" in response:
        # Note: Closing the stream is important because the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
        with closing(response["AudioStream"]) as stream:
            output = os.path.join(gettempdir(), "speech.mp3")

            try:
                # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)
    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)

    # Play the audio using the platform's default player
    st.audio(output, format="audio/mp3", autoplay=True)

    return output