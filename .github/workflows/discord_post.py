import os
import requests

def post_discord(text):
    url = os.getenv("DISCORD_WEBHOOK_URL")
    requests.post(url, json={"content": text})
