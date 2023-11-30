import openai
import os
from decouple import config
import certifi
certifi.where()



# Retrieve Environment Variables
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

## 2 attempts to troubleshoot max tries error
# openai.requests_ca_bundle = config("REQUESTS_CA_BUNDLE")
# os.environ['REQUESTS_CA_BUNDLE'] = './venv/lib/site-packages/certifi/cacert.pem'

# Open AI - Whisper (per Open AI docs)
# Convert Audio to Text
def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message_text = transcript["text"]
        return message_text
    except Exception as e:
        print(e)
        return