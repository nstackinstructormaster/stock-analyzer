
def trend_signal(close):
    close = close.dropna()

    if len(close) < 50:
        return "Insufficient data"

    price = close.iloc[-1]
    ma20 = close.tail(20).mean()
    ma50 = close.tail(50).mean()

    if price > ma20 > ma50:
        return "BUY"
    elif price < ma20 < ma50:
        return "SELL"
    return "HOLD"