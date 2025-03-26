from indicators import extract_features
from utils import get_symbols, process_symbol

def generate_all_signals():
    symbols = get_symbols()
    all_signals = {}
    for symbol in symbols:
        df, signals = process_symbol(symbol)
        all_signals[symbol] = signals
    return all_signals