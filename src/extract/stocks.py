import yfinance as yf

def get_stock(symbol, period="1mo"):
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period)
    df=df.reset_index()
    df["symbol"]=symbol
    return df

