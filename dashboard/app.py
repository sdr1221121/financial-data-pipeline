import streamlit as st
import duckdb
import pandas as pd

connection= duckdb.connect("data/warehouse/finance.db")

st.title("Financial Data Pipiline Dash")

df =connection.execute("SELECT * FROM prices").fetchdf()

assets= df["symbol"].unique()

selected_asset=st.sidebar.selectbox("choose one asset", assets)

filtered_df = df[df["symbol"]==selected_asset]

latest=filtered_df.iloc[-1]

col1, col2 =st.columns(2)

# METRIC1 current price
with col1:
    st.metric(" Current Price", latest["Close"])

# METRIC2 daily return
with col2:
    st.metric("Daily Return", latest["daily_return"])
    
#METRIC3 volatility

    
#GRAPHIC
st.subheader("Historical prices and moving averages")

chart_data=filtered_df.set_index("Date")
st.line_chart(chart_data[["Close","sma_7","sma_30"]])

#RECENT DATA TABLES
st.subheader("Last records")

st.dataframe(filtered_df.tail(10))
