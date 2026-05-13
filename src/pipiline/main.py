from src.extract.stocks import get_stock
from src.transform.indicators import transform
from src.load.duckdb_loader import load_data
from src.load.parquet_writer import save_parquet
from src.utils.logger import logger


ASSESTS=["AAPL","TSLA","NVDA","BTC-USD"]

def run_pipeline():
    for asset in ASSESTS:
        
        logger.info(f"Starting processement:{asset}")
                
        df=get_stock(asset)
        df=transform(df)
        save_parquet(df,asset)
        load_data(df)
        
        logger.info(f"{asset} processing was a sucess")
        
    
if __name__ == "__main__":
    logger.info("Pipeline Started")
    run_pipeline()
    logger.info("Pipeline was a sucess")