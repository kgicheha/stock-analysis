import requests
from bs4 import BeautifulSoup
import csv
from stockWatchList import stockWatchList
from termcolor import colored

stockFinancialResults = []

    # loops through watchlist and passes in stock to getSymbol function
def stocksInWatchList():
    for stock in stockWatchList:
        getStockSymbol(stock)

    # gets stocks symbol from watchList array
def getStockSymbol(stock):
    for key,value in stock.items():
        priceRequest(key, value['Ticker'], value['Target Price'] )

    # web scrap from yahoo to get prices
def priceRequest(stockName, ticker, targetPrice):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{ticker}'
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})["value"]

    # print(f"Current Stock Price for {stockName} is {price}")

    priceDifferenceCalculator(stockName, price, targetPrice)

# create function to see how far the stock price is from the target price
def priceDifferenceCalculator(stockName, price, targetPrice):

    priceDifference = round(float(price) - targetPrice, 2)

    stockFinancialResults.append({"Stock Name": stockName, "Current Price": price, "Target Price": targetPrice, "Price Difference" : priceDifference})
    createCsvFile()

    # gets information from stockFinancialResults array to create csv file
def createCsvFile():

    with open('stock_information.csv', mode ='w', newline='', encoding="utf-8-sig") as csvfile:
        fieldnames = ['Stock Name', 'Current Price', 'Target Price', 'Price Difference']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for stock in stockFinancialResults:
            writer.writerow(stock)

stocksInWatchList()
# print(stockFinancialResults)