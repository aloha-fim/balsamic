import openai
import os
from decouple import config

# Import custom functions
from functions.database import get_recent_messages

import certifi
certifi.where()


# Retrieve Environment Variables
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

## 3 attempts to troubleshoot max tries error
# openai.requests_ca_bundle = config("REQUESTS_CA_BUNDLE")
# os.environ['REQUESTS_CA_BUNDLE'] = './venv/lib/site-packages/certifi/cacert.pem'

# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "http://127.0.0.1:7890"

proxies = {'http': "http://127.0.0.1:7890",
           'https': "http://127.0.0.1:7890",
           'http': "http://127.0.0.1:21882",
           'https': "http://127.0.0.1:21882",
           'http': "http://127.0.0.1:55565",
           'https': "http://127.0.0.1:55565"
           }
openai.proxy = proxies


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

# Open AI - ChatGPT
# Get a response to our message
def get_chat_response(message_input):

    messages = get_recent_messages()
    user_message = {"role": "user", "content": message_input}
    messages.append(user_message)
    print(messages)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        print(response)
        message_text = response["choices"][0]["message"]["content"]
        return message_text
    except Exception as e:
        print(e)
        return
