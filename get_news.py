import yfinance as yf
from datetime import date
from stockList import stockNewsList


stockNewsResult = []


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker

    def getStockNews(self):

        current_stock = yf.Ticker(self.ticker)
        stock_news = current_stock.news
        print("Length", len(stock_news))

        for news in stock_news:
            title = news["title"]
            link = news["link"]
            publisher = news["publisher"]
            formatted_publish_date = date.fromtimestamp(
                news["providerPublishTime"])

            self.stockNewsResultsCompiler(
                title, link, publisher, formatted_publish_date)

    def stockNewsResultsCompiler(self, title, link, publisher, formatted_publish_date):

        stockNewsResult.append({
            "Ticker": self.ticker,
            "Title": title,
            "Link": link,
            "Published Date": formatted_publish_date,
            "Publisher": publisher
        })


def createNewsResult():
    if len(stockNewsList) > 0:
        for symbol in stockNewsList:
            processing_stock = Stock(symbol)
            processing_stock.getStockNews()
    else:
        print("Please add stock ticker(s) to the stockNewsList in the stockList.py file")


createNewsResult()

print(stockNewsResult)