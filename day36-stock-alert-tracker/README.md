# 📈Stock & News Alert Tracker (TSLA Example)

A Python script that tracks daily stock price movements using the Alpha Vantage API and pulls relevant news articles using the NewsAPI. When a significant price change occurs (±5% or more), the script outputs an alert along with related news headlines.

---

##  Features

- Fetches daily stock price data
- Calculates percentage change between trading days
- Detects significant price movements (±5% threshold)
- Pulls recent news articles related to the company
- Displays article titles and URLs for context

---

##  How It Works

1. Pulls daily stock data from **Alpha Vantage API**
2. Stores open and close prices by date
3. Compares price changes between consecutive days
4. If change ≥ 5%:
   - Triggers alert
   - Fetches related news from **NewsAPI**
   - Prints top articles

---

##  API Keys Needed

You must create free accounts and add your own API keys:

- 🔹 Alpha Vantage: https://www.alphavantage.co/support/#api-key
- 🔹 NewsAPI: https://newsapi.org/register

Then insert them into the script:

```python
STOCK_API_KEY = "your_alpha_vantage_key"
NEWS_API_KEY = "your_newsapi_key"
```

---

## Configuration

You can change the tracked stock here:

```python
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
```

Examples:
- AAPL → Apple
- MSFT → Microsoft
- NVDA → NVIDIA

---

## Example Output

```
ALERT: There was a 6.42% change in the stock between 2026-04-21 and 2026-04-20

Here is relevant news articles for Tesla Inc:

Source: Reuters
Title: Tesla shares jump after earnings report
URL: https://...
```

---

## Tech Stack

- Python 3
- Requests library
- Alpha Vantage API
- NewsAPI

---

## Future Improvements

- 📉 Add charts for stock movement
- 💬 Discord/Telegram bot integration
- ⏰ Automated daily alerts
- 📊 Multi-stock watchlist support
- 🧾 Export results to CSV

---

##  Disclaimer

This project is for educational purposes only. It is not financial advice.

---

## Author

Built by Anthony (Python learning project)
