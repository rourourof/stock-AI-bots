import yfinance as yf
import pandas as pd

def analyze(ticker):
    df = yf.download(ticker, period="30d", interval="1d", progress=False)
    last = df.iloc[-1]
    prev = df.iloc[-2]
    avg_vol = df["Volume"].rolling(20).mean().iloc[-1]

    return {
        "close": round(last["Close"], 2),
        "pct": round((last["Close"]/prev["Close"]-1)*100, 2),
        "high": round(last["High"], 2),
        "low": round(last["Low"], 2),
        "vol": int(last["Volume"]),
        "vol_avg": int(avg_vol),
        "vol_above_avg": last["Volume"] >= avg_vol,
        "break_high": last["High"] > prev["High"],
        "break_low": last["Low"] < prev["Low"],
    }

def get_market_data():
    nvda = analyze("NVDA")
    sox = analyze("^SOX")
    nasdaq = analyze("^IXIC")

    return {
        "NVDA": nvda,
        "SOX": sox,
        "NASDAQ": nasdaq
    }
