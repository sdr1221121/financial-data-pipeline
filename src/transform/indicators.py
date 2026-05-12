def add_daily_return(df):
    df["daily_return"] = df["Close"].pct_change()
    return df

def add_moving_average(df, window=7):
    df[f"sma_{window}"]= df["Close"].rolling(window).mean()
    return df

def transform(df):
    df= add_daily_return(df)
    
    df=add_moving_average(df)
    
    df= add_moving_average(df,30)
    return df




# Column explanations:
# Open         -> stock opening price
# High         -> highest price of the day
# Low          -> lowest price of the day
# Close        -> stock closing price
# Volume       -> trading volume
# Dividends    -> dividends paid
# Stock Splits -> stock split events
# symbol       -> stock ticker symbol (e.g. AAPL)
# daily_return -> daily percentage return
# sma_7        -> 7 day simple moving average
# sma_30       -> 30 day simple moving average

if __name__ == "__main__":
    from src.extract.stocks import get_stock
    
    print("A iniciar transform layer...")
    
    df=get_stock("AAPL")
    
    df=transform(df)
    
    print(df.head)
    
    print("Transform concluido com sucesso")
    