
Project Description:
    These Python scripts empower users to perform swift technical analysis through workflow automation.

    If done manually, performing technical analysis on stocks can be a time-consuming and repetitive task.

    These scripts significantly reduce the time required for performing technical analysis by automating the steps of aggregating stock data and news, and delivering the results in a CSV file format which is very useful when working other programs such as Miscrosoft Excel.

    The scripts can be used to gather either or multiple stocks within a few seconds.

    The Yahoo Finance library is leveraged to aggregate real-time market data and news.

    With the files readily available, users can swiftly conduct their analysis, saving valuable time.

How To Run the Scripts:
1) Download the repository to your local machine.
2) Go to the folder where the files are stored in your local machine
3) run python3 <<name of file>>

Description of each File:

    financials.py Script
        To specify which stock you want to research, add the stock ticker to the stockList array in the 'stockList.py' file
        Once sucessfully run, a cvs file called 'stock-analysis-{current date}' will downloaded in the folder.
        Open the file to view the data.

    get_news.py Script
        To specify the stock you want the news for, add the stock ticker to the stockNewsList array in the 'stockList.py' file
        Once sucessfully run, a cvs file called 'stock-news-{current date}' will downloaded in the folder.
        Open the file to view the news.

    create_chart.py Script
        Utilizes the Matplotlib library to create visually engaging price and volume charts for enhanced data visualization.
        When running this script, you will be prompted to type in the stock ticker you want the chart for.
        Please be sure to type in the correct ticker.
        When run successfully, the chart will automatically open.

    comparison.py Script
        Use this script to compare the stock prices for multiple stocks.
        To specify the stocks you want to compare, add the stock ticker to the stocksToCompare array in the 'stockList.py' file
        When run successfully, the chart will automatically open.

**Disclaimer**:
    Please do your own research and consult with a financial advisor before making any investment.
    This is only a personal project that I'm using the learn about automation and data analysis using python


