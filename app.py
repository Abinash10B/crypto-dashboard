"""
Live Crypto Price Dashboard
----------------------------
A simple, beginner-friendly Streamlit app that pulls live cryptocurrency
price data from the CoinGecko public API, cleans it with pandas, and
displays it as an interactive dashboard.

Author: <your name here>
"""

import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# -------------------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------------------
st.set_page_config(page_title="Live Crypto Dashboard", page_icon="📈", layout="centered")

st.title("📈 Live Crypto Price Dashboard")
st.caption("Real-time price data pulled from the CoinGecko API, analyzed with pandas.")

# -------------------------------------------------------------------
# STEP 1: PULL LIVE DATA FROM THE API
# -------------------------------------------------------------------
COINS = ["bitcoin", "ethereum", "solana", "dogecoin", "cardano"]

@st.cache_data(ttl=60)  # cache for 60 seconds so we don't hammer the API on every click
def get_price_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(COINS),
        "vs_currencies": "usd",
        "include_24hr_change": "true",
        "include_market_cap": "true",
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

# -------------------------------------------------------------------
# STEP 2: CLEAN / STRUCTURE THE DATA WITH PANDAS
# -------------------------------------------------------------------
def build_dataframe(raw_data):
    df = pd.DataFrame(raw_data).T.reset_index()
    df.columns = ["Coin", "Price (USD)", "Market Cap (USD)", "24h Change (%)"]
    df["Coin"] = df["Coin"].str.capitalize()
    df["24h Change (%)"] = df["24h Change (%)"].round(2)
    df["Price (USD)"] = df["Price (USD)"].round(2)
    return df

try:
    raw = get_price_data()
    df = build_dataframe(raw)
except Exception as e:
    st.error(f"Couldn't fetch live data right now: {e}")
    st.stop()

st.caption(f"Last updated: {datetime.now().strftime('%I:%M:%S %p')} (refreshes every 60s on interaction)")

# -------------------------------------------------------------------
# STEP 3: INTERACTIVE FILTER
# -------------------------------------------------------------------
selected_coin = st.selectbox("Choose a coin to inspect", df["Coin"])
row = df[df["Coin"] == selected_coin].iloc[0]

# -------------------------------------------------------------------
# STEP 4: KPI CARDS
# -------------------------------------------------------------------
col1, col2, col3 = st.columns(3)
col1.metric("Price (USD)", f"${row['Price (USD)']:,.2f}")
col2.metric("24h Change", f"{row['24h Change (%)']}%", delta=f"{row['24h Change (%)']}%")
col3.metric("Market Cap", f"${row['Market Cap (USD)']:,.0f}")

# -------------------------------------------------------------------
# STEP 5: FULL TABLE + CHART
# -------------------------------------------------------------------
st.subheader("All Tracked Coins")
st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("Price Comparison")
st.bar_chart(df.set_index("Coin")["Price (USD)"])

st.subheader("24h Change Comparison")
st.bar_chart(df.set_index("Coin")["24h Change (%)"])

# -------------------------------------------------------------------
# STEP 6: SIMPLE INSIGHT FLAG (no AI needed, but AI could replace this)
# -------------------------------------------------------------------
top_mover = df.loc[df["24h Change (%)"].abs().idxmax()]
direction = "up" if top_mover["24h Change (%)"] > 0 else "down"
st.info(
    f"📊 **Insight:** {top_mover['Coin']} is today's biggest mover, "
    f"{direction} {abs(top_mover['24h Change (%)'])}% in the last 24 hours."
)
