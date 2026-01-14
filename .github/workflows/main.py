import os
import datetime
import pytz
from market_data import get_market_data
from scenario import load_prev_scenario, save_scenario
from ai_writer import generate_text
from discord import post_discord
from fallback import fallback_text

JST = pytz.timezone("Asia/Tokyo")
now = datetime.datetime.now(JST)
hour = now.hour

MODE = "1807" if hour >= 18 else "0607"

try:
    data = get_market_data()
    prev = load_prev_scenario() if MODE == "0607" else None
    text = generate_text(data, MODE, prev)
except Exception as e:
    text = fallback_text(data if 'data' in locals() else None)

post_discord(text)

if MODE == "1807":
    save_scenario(text)
