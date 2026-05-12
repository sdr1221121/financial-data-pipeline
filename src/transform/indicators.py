import pandas as pd

def add_daily_return(df):
    df["daily_return"] = df["Close"].pct_change()
    return df

def add_moving_average(df, window=7):
    df[f"sma_{window}"]= df["Close"].rolling(window).mean()