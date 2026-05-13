import os

def save_parquet(df, symbol):
    os.makedirs("data/raw", exist_ok=True)
    
    path=f"data/raw/{symbol}.parquet"
    
    df.to_parquet(path, index=False)
    
    print(f"saved data in:{path}")