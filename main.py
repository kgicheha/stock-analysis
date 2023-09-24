import requests
from bs4 import BeautifulSoup
import csv
from stockList import stockList
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

    stockResultsCompile(stockName, ticker, currentPrice, targetPrice,
                        beta, peRatio, dividendYield, yearEstimatePrice, marketCap)


#  function appends stock information to a results array
def stockResultsCompile(stockName, ticker, currentPrice, targetPrice, beta, peRatio, dividendYield, yearEstimatePrice, marketCap):

    currentPrice = round(float(currentPrice),2)
    targetPrice = round(targetPrice, 2)

    priceDifference = round(currentPrice - targetPrice, 2)

    if priceDifference > 0:
        indicator = "Wait To Buy"
    else:
        indicator = "Buy Now"

    stockFinancialResults.append({"Stock Name": stockName,
                                  "Ticker": ticker,
                                  "Beta": beta,
                                  "PE Ratio": peRatio,
                                  "Dividend Yield": dividendYield,
                                  "1y Target Estimate": yearEstimatePrice,
                                  "Current Price": currentPrice,
                                  "Target Entry Price": targetPrice,
                                  "Price Difference": priceDifference,
                                  "Wait/Buy Now": indicator})
    createCsvFile()


# gets information from stockFinancialResults array to create csv file
def createCsvFile():

    today = str(date.today())
    fileNameFormat = "stock-watchlist-" + today + ".csv"

    with open(f'{fileNameFormat}', mode='w', newline='', encoding="utf-8-sig") as csvfile:
        fieldnames = ['Stock Name', 'Ticker', 'Beta', 'PE Ratio', 'Dividend Yield', '1y Target Estimate', 'Current Price',
                      'Target Entry Price', 'Price Difference', 'Wait/Buy Now']
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

        # prints out the data from the stock Financial Results
        for stock in stockFinancialResults:
            writer.writerow(stock)


stocksInWatchList()
# print(stockFinancialResults)
print("File has been successfully created!")


# ADD CURRENT DATE AND TIME TO CSV FILE