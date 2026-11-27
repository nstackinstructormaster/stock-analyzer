import streamlit as st
import yfinance as yf

st.title("Stock Analyzer")
symbol = st.text_input("Stock symbol", "AAPL")
data = yf.Ticker(symbol).history(period="5d")

if data.empty:
    st.warning("No price data found.")
else:
    st.metric("Latest Closing Price", f"{data['Close'].iloc[-1]:,.2f}")