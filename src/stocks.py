import yfinance as yf


DEFAULT_STOCKS = ["000300.SS", "000001.SS"]

def fetch_stocks(symbols: list[str] | None = None) -> list[dict]:
    symbols = symbols or DEFAULT_STOCKS
    results = []

    for symbol in symbols:
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="1d")
            if hist.empty:
                continue

            close = hist["Close"].iloc[-1]
            prev_close = hist["Close"].iloc[0] if len(hist) > 1 else close
            change_pct = ((close - prev_close) / prev_close) * 100

            info = ticker.fast_info
            name = getattr(info, "previous_close", symbol)
            results.append({
                "symbol": symbol,
                "price": round(close, 2),
                "change_pct": round(change_pct, 2),
            })
        except Exception:
            results.append({
                "symbol": symbol,
                "price": None,
                "change_pct": None,
            })

    return results
