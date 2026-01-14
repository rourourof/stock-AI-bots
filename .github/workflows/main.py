import datetime
import pytz

from market_data import get_market_data
from scenario import load_prev_scenario, save_scenario
from gemini_writer import generate_text
from discord_post import post_discord
from fallback import fallback_text

JST = pytz.timezone("Asia/Tokyo")
now = datetime.datetime.now(JST)

MODE = "1807" if now.hour >= 18 else "0607"

try:
    data = get_market_data()
    prev = load_prev_scenario() if MODE == "0607" else None
    text = generate_text(data, MODE, prev)
except Exception:
    text = fallback_text(locals().get("data"))

post_discord(text)

if MODE == "1807":
    save_scenario(text)
