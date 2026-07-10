#!/usr/bin/env python3
import ollama 
import time
import requests
from ollama import Client
import os 
OLLAMA_API_KEY = os.environ["OLLAMA_API_KEY"]
WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]
client = Client(
    host="https://ollama.com/api",
    headers={"Authorization": f"Bearer {OLLAMA_API_KEY}"}
)

response1 = ollama.generate(
    model="gpt-oss:120b-cloud",
    system="you are quote generator only respond with a quote and a citation",
    prompt="what is a niche and profound philosophy quote"
)
content=(response1.response)
payload = {
    "content": content
}
try:
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 204:
        print("Quote sent successfully!")
    else:
        print(f"Failed to send. Server responded with status: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")

