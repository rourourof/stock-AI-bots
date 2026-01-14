import yfinance as yf

def analyze(symbol):
    df = yf.download(symbol, period="30d", interval="1d", progress=False)
    last = df.iloc[-1]
    prev = df.iloc[-2]
    vol_avg = df["Volume"].rolling(20).mean().iloc[-1]

    return {
        "close": round(last["Close"], 2),
        "pct_change": round((last["Close"] / prev["Close"] - 1) * 100, 2),
        "high": round(last["High"], 2),
        "low": round(last["Low"], 2),
        "volume": int(last["Volume"]),
        "volume_avg_20": int(vol_avg),
        "volume_above_avg": last["Volume"] >= vol_avg,
        "break_prev_high": last["High"] > prev["High"],
        "break_prev_low": last["Low"] < prev["Low"],
    }

def get_market_data():
    return {
        "NVDA": analyze("NVDA"),
        "SOX": analyze("^SOX"),
        "NASDAQ": analyze("^IXIC")
    }
