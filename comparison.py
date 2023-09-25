import matplotlib.pyplot as plt
import yfinance as yf
from stockList import stocksToCompare

# used to store the results of each stock
stockFinancialResults = []

# fetches data from yahoo finance, then appends it to the results array
def fetchData(ticker):
    current_stock = yf.Ticker(ticker)
    current_stock_info = current_stock.info

    stock_history = current_stock.history(period="max")

    stock_close = stock_history["Close"]
    symbol = current_stock_info["symbol"]
    stock_index = stock_history.index

    stockFinancialResults.append(
        {"Symbol": symbol, "Close Price": stock_close, "Stock Index": stock_index})


# creates the chart
def createChart():

    # Create a figure for plotting
    plt.figure(figsize=(12, 6))

    # Plot the stock prices for each symbol
    for stock in stockFinancialResults:
        plt.plot(stock["Stock Index"], stock["Close Price"],
                 label=stock["Symbol"])

    # Customize the chart
    plt.title("Stock Price Comparison")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.legend()
    plt.grid(True)

    # Display the chart
    plt.show()


# gets data from the stockList.py file
def stockCompareChart():
    if len(stocksToCompare) > 1:
        for symbol in stocksToCompare:
            fetchData(symbol)
            print("Fetching Data for", symbol)
    else:
        print(
            "Please add stock tickers to the stocksToCompare array in the stockList.py file")


stockCompareChart()
createChart()
