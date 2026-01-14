import requests
import os

def post_discord(text):
    url = os.getenv("DISCORD_WEBHOOK_URL")
    requests.post(url, json={"content": text})
