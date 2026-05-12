import duckdb

connection= duckdb.connect("data/warehouse/finance.db")

def create_table():
    connection.execute("""
    CREATE TABLE IF NOT EXISTS prices(
        Date TIMESTAMP,
        Open DOUBLE,
        High DOUBLE,
        Low DOUBLE,
        Close DOUBLE,
        Volume DOUBLE,
        Dividends DOUBLE,
        "Stock Splits" DOUBLE,
        symbol VARCHAR,
        daily_return DOUBLE,
        sma_7 DOUBLE,
        sma_30 DOUBLE
        )
        """)

def load_data(df):
    create_table()
    connection.register("df", df)
    connection.execute("INSERT INTO prices SELECT * FROM df")
    
if  __name__=="__main__":
    from src.extract.stocks import get_stock
    from src.transform.indicators import transform
    
    print("loading layer")
    df=get_stock("AAPL")
    df=transform(df)
    load_data(df)
    print("its finished - data saved in DuckDB")