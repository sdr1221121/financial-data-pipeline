import pandas as pd

path="data/raw/AAPL.parquet"

df=pd.read_parquet(path)

print(df.columns)

print(df.head(20))

print(df.dtypes)

