import streamlit as st
import yfinance as yf
from signals import trend_signal

st.title("AI Stock Analyzer")
symbol = st.text_input("Stock symbol", "AAPL")
data = yf.Ticker(symbol).history(period="6mo")

if data.empty:
    st.warning("No price data found.")
else:
    st.metric("Latest Closing Price", f"{data['Close'].iloc[-1]:,.2f}")
    st.line_chart(data["Close"])
    st.metric("Trend Signal", trend_signal(data["Close"]))

st.caption("Powered by Yahoo Finance")
    