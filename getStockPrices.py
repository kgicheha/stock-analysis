import requests
from bs4 import BeautifulSoup


stockWatchList = [{
    "Apple": {
       "Ticker" : "AAPL",
       "Target Price": 150
    },
    "Microsoft": {
       "Ticker" : "MSFT",
       "Target Price": 300
    },

}]

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
        print("Getting Price for: ", key)
        # print(value['Ticker'])
        priceRequest(value['Ticker'])

def priceRequest(ticker):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{ticker}'
    response = requests.get(url, headers=headers)
    # print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})["value"]

    print(price)

stocksInWatchList()