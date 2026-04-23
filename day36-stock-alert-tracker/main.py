import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL = "https://www.alphavantage.co/query?"
STOCK_API_KEY = ""
NEWS_URL = "https://newsapi.org/v2/everything?"
NEWS_API_KEY = ""
STOCK_PARAMS = {"function": "TIME_SERIES_DAILY",
                "symbol": STOCK,
                "outputsize": "compact",
                "datatype": "json",
                "apikey": STOCK_API_KEY}
from_date = ""
to_date = ""
NEWS_PARAMS = {"apiKey": NEWS_API_KEY,
               "q": COMPANY_NAME,
               "searchIn": "title,description",
               "from": from_date,
               "to": to_date,
               "language": "en",
               "pageSize": 3}
stock_num = {}
prev_date_close = 0
prev_date = ""

def percent_change(n1, n2):
    return (n2 - n1) / n1 * 100

def get_stock_data():
    response = requests.get(url=STOCK_URL, params=STOCK_PARAMS)
    response.raise_for_status()
    stock_data = response.json()
    for date_data in stock_data['Time Series (Daily)']:
        stock_num[date_data] = {'open': stock_data['Time Series (Daily)'][date_data]['1. open'],
                                 'close': stock_data['Time Series (Daily)'][date_data]['4. close'] }
    return stock_num

def get_news_articles():
    response = requests.get(url=NEWS_URL, params=NEWS_PARAMS)
    response.raise_for_status()
    news_data = response.json()
    for article in news_data['articles']:
        print(f"Source: {article['source']['name']}")
        print(f"Author: {article['author']}")
        print(f"Title: {article['title']}")
        print(f"URL: {article['url']}\n")

stock_info = get_stock_data()

for date in stock_info:
    date_open = float(stock_info[date]['open'])
    if prev_date_close != 0:
        if percent_change(date_open, prev_date_close) >= 5 or percent_change(date_open, prev_date_close) <= -5:
            print(f"ALERT: There was a {percent_change(date_open, prev_date_close):.2f}% change in the stock between {date} and {prev_date}")
            print(f"Here is relevant news articles for {COMPANY_NAME} from {date} to {prev_date}:\n")
            from_date = date
            to_date = prev_date
            get_news_articles()

    prev_date = date
    prev_date_close = float(stock_info[date]['close'])
