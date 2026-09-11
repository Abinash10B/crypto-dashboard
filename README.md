# 📈 Live Crypto Price Dashboard

An interactive web dashboard that pulls **real-time cryptocurrency prices**
from a public API, cleans and structures the data with pandas, and displays
it through a Streamlit dashboard with live KPIs, charts, and an auto-generated
insight.

---

## 1. Problem Statement

Crypto prices change every second, and most beginner data projects rely on
static, pre-downloaded CSV files — which don't reflect how analysts actually
work with live, constantly-changing data in the real world.

This project solves that by building a lightweight tool that:
- Pulls **live** price data directly from an API (no manual downloads)
- Cleans and structures it automatically
- Surfaces the most important numbers (price, 24h change, market cap) in a
  clear, glanceable format
- Flags the day's most significant price movement without the user having
  to dig through the table themselves

---

## 2. Objective

- Practice pulling data from a live, public API
- Clean and reshape raw JSON into a usable pandas DataFrame
- Build an interactive, filterable dashboard (not just a static chart)
- Deploy the project as a live, shareable link — not just code on GitHub

---

## 3. Tools & Technologies Used

| Tool | Purpose |
|---|---|
| **Python** | Core programming language |
| **Pandas** | Data cleaning and transformation |
| **Requests** | Pulling live data from the CoinGecko API |
| **Streamlit** | Building the interactive web dashboard |
| **CoinGecko API** | Free, no-key-required live crypto price data |
| **GitHub + Streamlit Community Cloud** | Hosting and free deployment |

---

## 4. Project Structure

```
crypto-dashboard/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation (this file)
```

---

## 5. How the Project Works (Step by Step)

1. **Data pull** — `requests` calls the CoinGecko `/simple/price` endpoint
   for 5 coins (Bitcoin, Ethereum, Solana, Dogecoin, Cardano), requesting
   price, 24h % change, and market cap.
2. **Data cleaning** — The raw JSON is converted into a pandas DataFrame,
   columns are renamed and rounded, and coin names are formatted for display.
3. **Caching** — `@st.cache_data(ttl=60)` prevents hitting the API on every
   single interaction, refreshing only once per minute — a simple but
   realistic rate-limiting practice.
4. **Interactivity** — A dropdown lets the user pick a coin to inspect in
   detail via KPI cards (price, 24h change, market cap).
5. **Visualization** — Two bar charts compare price and 24h performance
   across all tracked coins.
6. **Insight generation** — The app automatically identifies and calls out
   the day's biggest mover, so the user doesn't have to scan the table
   themselves.

---

## 6. How to Run Locally

```bash
# 1. Clone or download this folder, then navigate into it
cd crypto-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## 7. How to Deploy (Free)

1. Push this folder to a public GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub, select the repo and `app.py`
4. Click **Deploy** — you'll get a live public link in a couple of minutes

---

## 8. Key Insights

- Live price data can swing significantly even within a single testing
  session, which is exactly why caching and clear "last updated" timestamps
  matter for any real-time dashboard.
- Market cap and price movement don't always correlate — a coin can have a
  small price and still be a top mover in percentage terms, which is why
  showing both metrics side by side is more useful than price alone.
- Automating the "what changed the most" insight removes the need for the
  user to manually scan a table, which is a small but meaningful UX
  improvement analysts should think about when building any dashboard.

---

## 9. Future Improvements

- Add historical price charts (line chart over time) by logging each
  refresh into a running dataset
- Replace the rule-based insight with an **AI-generated** natural-language
  summary (e.g., using the Claude or OpenAI API) for richer commentary
- Add price alert thresholds with conditional formatting/notifications
- Expand to more coins or let the user add their own ticker

---

## 10. Conclusion

This project demonstrates an end-to-end, real-world data analyst workflow:
sourcing live data via an API, cleaning it programmatically, and presenting
it through an interactive, deployable dashboard — rather than relying on a
static, pre-cleaned dataset. It's intentionally kept simple so the core
skills (API integration, pandas, and interactive visualization) are clear
and easy to explain in an interview, while leaving clear room to extend
further (AI commentary, historical trends, alerts) as a natural next step.
