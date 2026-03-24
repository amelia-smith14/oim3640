import yfinance as yf

stock = yf.Ticker("AAPL")
info = stock.info
print(info['shortName'])
print(info['currentPrice'])

info = yf.Ticker("AAPL").info