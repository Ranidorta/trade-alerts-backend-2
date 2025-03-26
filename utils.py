import requests
import pandas as pd

BYBIT_API_URL = "https://api.bybit.com/v5/market/kline"
INTERVAL = "1h"
CANDLE_LIMIT = 200

def get_symbols():
    url = "https://api.bybit.com/v5/market/instruments-info"
    params = {"category": "linear"}
    res = requests.get(url, params=params)
    data = res.json()
    symbols = [x["symbol"] for x in data["result"]["list"] if "USDT" in x["symbol"]]
    return symbols

def get_candles(symbol, interval="1h", limit=200):
    params = {"category": "linear", "symbol": symbol, "interval": interval, "limit": limit}
    res = requests.get(BYBIT_API_URL, params=params)
    data = res.json()
    candles = data["result"]["list"]
    df = pd.DataFrame(candles, columns=[
        "timestamp", "open", "high", "low", "close", "volume", "turnover"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df[["open", "high", "low", "close"]] = df[["open", "high", "low", "close"]].astype(float)
    return df

def process_symbol(symbol):
    df = get_candles(symbol)
    if df.empty:
        return df, []
    df = extract_features(df)
    df = df.dropna()
    df["signal"] = df["RSI_14"].apply(lambda x: 1 if x < 30 else -1 if x > 70 else 0)
    latest_signals = df[["timestamp", "close", "signal"]].tail(5).to_dict(orient="records")
    return df, latest_signals