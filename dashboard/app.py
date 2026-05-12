import streamlit as st
import duckdb
import pandas as pd

connection= duckdb.connect("data/warehouse/finance.db")

st.title("Financial Data Pipiline Dash")

df =connection.execute("SELECT * FROM prices").fetchdf()

st.subheader("Close Price")
st.line_chart(df.set_index("Date")["Close"])

st.subheader("Recent Data")
st.dataframe(df.tail(20))