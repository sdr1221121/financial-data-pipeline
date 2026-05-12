from src.extract.stocks import get_stock
from src.transform.indicators import transform
from src.load.duckdb_loader import load_data

def run_pipeline(symbol:str):
    print(f"processing {symbol}")
    
    df=get_stock(symbol)
    df=transform(df)
    load_data(df)
    
    print(f"{symbol} processing was a sucess")
    
    
if __name__ == "__main__":
    print("start")
    
    assests=["AAPL","TSLA","NVDA"]
    
    for asset in assests:
        run_pipeline(asset)
        
    print("pipeline was a sucess")