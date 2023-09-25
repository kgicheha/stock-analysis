import yfinance as yf
from datetime import date
from stockList import stockNewsList
import csv
import os
import sys

stockNewsResult = []


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker

    def getStockNews(self):

        print(f"Fetching news for {self.ticker} ...")

        current_stock = yf.Ticker(self.ticker)
        current_stock_info = current_stock.info

        stock_name = current_stock_info["shortName"]
        stock_news = current_stock.news


        for news in stock_news:
            title = news["title"]
            link = news["link"]
            publisher = news["publisher"]
            formatted_publish_date = date.fromtimestamp(
                news["providerPublishTime"])

            self.stockNewsResultsCompiler(
                stock_name, title, link, publisher, formatted_publish_date)

        print(f"Sucessfully fetched the news {self.ticker}")

    def stockNewsResultsCompiler(self, stock_name, title, link, publisher, formatted_publish_date):

        stockNewsResult.append({
            "Company Name": stock_name,
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


def createCsvFile():

    today = str(date.today())
    fileNameFormat = "stock-news-" + today + ".csv"

    with open(f'{fileNameFormat}', mode='w', newline='', encoding="utf-8-sig") as csvfile:
        fieldnames = [
            "Company Name",
            "Ticker",
            "Title",
            "Link",
            "Published Date",
            "Publisher"
        ]
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

        # prints out the data from the stock Financial Results
        for stock in stockNewsResult:
            writer.writerow(stock)

    print("Successfully created the News File. Please Check folder")

    # to automatically open file file once its created in read-only
    fd = os.open(f"./{fileNameFormat}", os.O_RDWR)

if len(stockNewsResult) > 0:
    createCsvFile()
