import requests
from bs4 import BeautifulSoup
import csv
from stockWatchList import stockWatchList

stockFinancialResults =[]
# loop through each item in the stock list object
#   pass in the ticker to the url
    # return the price of each item

    # loops through watchlist and passes in stock to getSymbol function
def stocksInWatchList():
    for stock in stockWatchList:
        getStockSymbol(stock)

    # gets stocks symbol from watchList array
def getStockSymbol(stock):
    for key,value in stock.items():
        priceRequest(key, value['Ticker'])

def priceRequest(stockName, ticker):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{ticker}'
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})["value"]

    print(f"Current Stock Price for {stockName} is {price}")

    # stockFinancialResults.append({f'Stock Name': {stockName}, "Price": {price}"})
    # createCsvFile(stockName, price)


    # create csv file for the stocks
# def createCsvFile(stockName, price):
#     with open('stock_information.csv', mode ='w') as csvfile:
#         fieldnames = ['Stock Name', 'Current Price']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerow(stockName, price)


stocksInWatchList()