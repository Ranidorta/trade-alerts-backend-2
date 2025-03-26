import pandas_ta as ta

def extract_features(df):
    df.ta.rsi(length=14, append=True)
    df.ta.macd(append=True)
    df.ta.sma(length=20, append=True)
    df.ta.ema(length=50, append=True)
    return df