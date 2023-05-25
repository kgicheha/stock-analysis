
Project Description:
    This script allows you to create a watchlist of stocks you're interested in investing and price you want the stock to get to before making an investment in the company.
    The idea came about from my interest in investing, however I didnt want to check on each individual stock daily to see whether the current price is below my desired entry price.
    Having to check each stock individually is tedius and very redundant.
    So I decided to automate this process using a Python script.
    Now all I have to do is to add the company's that I'm interested in and the target price that I would like the stock to get to before making an investment.
    The script using Beautifulsoup library to web scrape data of the companies that I have on my watchlist and then creates a csv file with the key information,
    including whether I should invest based on if the stock price has reached my desired entry price.


Issue This Project Helps To Solve:
    Rather than researching each stock at a time to see whether the stock price has reached your desired buy in price. This script helps you to automate that.

How To Run The Script:

1. Clone the repository down to your local computer

2. Change the User-agent that's in the stockInfoRequest function (in the getStockPrices.py file) to your own computer:
    You can find this information by googling "User-Agent"
    Copy and past the result to the inside the stockInfoRequest function

3. Add the company stocks that you're interested in investing in to the stockWatchList.py file
    Use the samples that are in the files to format the stocks
    Set the price that you want the stock to drop to so that you invest in it
        To get a target entry price, you can simply research a company's all-time high stock price
        Then calculate a target price that's below that all-time high price.

4. Save the files and then Run the getStockPrices.py file in the command line using following:
        python3 getStockPrices.py

5. If everything ran sucessfully:
    You will see a new csv file in the folder that has the results.
    The results will feature:
        1. Key company data, like the current stock price
        2. How far the current stock price is from your'e desired entry price.
        3. Indicator on whether you should buy the stock or wait, based on if the current stock price is equal to or below you're target entry price.


Python libraries used for this project
    1. Beautiful Soup is a Python library for pulling data out of HTML and XML files


**Disclaimer**:
    Please do your own research and consult with a financial advisor before making any investment.
    This is only a personal project that I'm using the learn about webscraping


