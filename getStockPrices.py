import requests
from bs4 import BeautifulSoup
import csv
from stockWatchList import stockWatchList
from termcolor import colored
from datetime import date

stockFinancialResults = []

# loops through watchlist and passes in stock to getSymbol function
def stocksInWatchList():
    for stock in stockWatchList:
        getStockInformation(stock)


# gets stocks symbol from watchList array
def getStockInformation(stock):
    for key, value in stock.items():
        stockInfoRequest(key, value['Ticker'], value['Target Price'])


# web scrap from yahoo to get prices
def stockInfoRequest(stockName, ticker, targetPrice):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{ticker}'
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    currentPrice = soup.find(
        'fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})["value"]
    beta = soup.find('td', {'class': "Ta(end) Fw(600) Lh(14px)",
                     'data-test': "BETA_5Y-value"}).get_text(strip=True)
    peRatio = soup.find('td', {'class': "Ta(end) Fw(600) Lh(14px)",
                        'data-test': "PE_RATIO-value"}).get_text(strip=True)
    dividendYield = soup.find('td', {'class': "Ta(end) Fw(600) Lh(14px)",
                              'data-test': "DIVIDEND_AND_YIELD-value"}).get_text(strip=True)
    yearEstimatePrice = soup.find('td', {'class': "Ta(end) Fw(600) Lh(14px)",
                                  'data-test': "ONE_YEAR_TARGET_PRICE-value"}).get_text(strip=True)
    marketCap = soup.find('td', {'class': "Ta(end) Fw(600) Lh(14px)",
                          'data-test': "MARKET_CAP-value"}).get_text(strip=True)

    stockResultsCompile(stockName, currentPrice, targetPrice,
                        beta, peRatio, dividendYield, yearEstimatePrice, marketCap)


#  function appends stock information to a results array
def stockResultsCompile(stockName, currentPrice, targetPrice, beta, peRatio, dividendYield, yearEstimatePrice, marketCap):

    priceDifference = round(float(currentPrice) - targetPrice, 2)

    if priceDifference > 0:
        indicator = "Wait To Buy"
    else:
        indicator = "Buy Now"

    stockFinancialResults.append({"Stock Name": stockName,
                                  "Beta": beta,
                                  "PE Ratio": peRatio,
                                  "Dividend Yield": dividendYield,
                                  "Current Price": currentPrice,
                                  "1y Target Estimate": yearEstimatePrice,
                                  "Target Entry Price": targetPrice,
                                  "Price Difference": priceDifference,
                                  "Wait/Buy Now": indicator})
    createCsvFile()



# gets information from stockFinancialResults array to create csv file
def createCsvFile():

    with open('stock_information.csv', mode='w', newline='', encoding="utf-8-sig") as csvfile:
        fieldnames = ['Stock Name', 'Beta', 'PE Ratio', 'Dividend Yield', 'Current Price', '1y Target Estimate',
                      'Target Entry Price', 'Price Difference', 'Wait/Buy Now']
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

        # prints out current date
        today = date.today()
        dateFormat  = f'Today Date {today}'
        writer.writerow(dateFormat)

        # prints out the data from the stock Financial Results
        for stock in stockFinancialResults:
            writer.writerow(stock)


stocksInWatchList()
# print(stockFinancialResults)
print("File has been successfully updated!")


# ADD CURRENT DATE AND TIME TO CSV FILE