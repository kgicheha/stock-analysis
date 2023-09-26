
Project Description:
    These Python scripts empower users to make informed decisions in stock investments through automated technical analysis.

    Performing manual technical analysis on stocks can be a time-consuming and repetitive task.

    These scripts significantly reduce the time required for technical analysis by automating the research process, aggregating real-time stock data and news for multiple stocks, and delivering the results in a convenient CSV file format within seconds.

    With the files readily available, users can swiftly conduct their analysis, saving valuable time.


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


