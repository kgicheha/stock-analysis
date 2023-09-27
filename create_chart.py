import yfinance as yf
import matplotlib.pyplot as plt

class CreateStockChart:
    def __init__(self, ticker):
        self.ticker = ticker

    def fetchData(self):

        # Fetch the stock price data using yfinance
        current_stock = yf.Ticker(self.ticker)
        current_stock_info = current_stock.info

        stock_name = current_stock_info["shortName"]
        symbol = current_stock_info["symbol"]
        currency = current_stock_info["currency"]

        stock_history = current_stock.history(period="max")

        stock_close = stock_history["Close"]
        stock_volume = stock_history["Volume"]
        stock_index = stock_history.index

        self.createChart(stock_close, symbol, currency, stock_index, stock_volume)


    def createChart(self, stock_close, symbol, currency, stock_index, stock_volume):
        # Create a figure with multiple subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

        # Plot the stock price chart
        ax1.plot(stock_index, stock_close, label="Close Price", color="blue")
        ax1.set_title(f"{symbol} Stock Price")
        ax1.set_ylabel(f"Price({currency})")
        ax1.grid(True)
        ax1.legend()

        # Plot the stock volume chart
        ax2.fill_between(stock_index, stock_volume, color="gray", alpha=0.6)
        ax2.set_title(f"{symbol} Stock Volume")
        ax2.set_xlabel("Date")
        ax2.set_ylabel("Volume")
        ax2.grid(True)

        # displays chart
        plt.tight_layout()
        plt.show()


user_input = input("Enter stock ticker: ")
stock_chart = CreateStockChart(user_input)
stock_chart.fetchData()
print(f"Successfully fetched data for {user_input}")