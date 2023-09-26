
Project Description:
    These Python scripts empower users to make informed decisions in stock investments through automated technical analysis.

    Performing manual technical analysis on stocks can be a time-consuming and repetitive task.

    These scripts significantly reduce the time required for technical analysis by automating the research process, aggregating real-time stock data and news for multiple stocks, and delivering the results in a convenient CSV file format within seconds.

    With the files readily available, users can swiftly conduct their analysis, saving valuable time.

How To Run the Scripts:
1) Download the repository to your local machine.
2) Go to the folder where the files are stored in your local machine
3) run python3 <<name of file>>

Description of each File:

    financials.py Script
        Leverages the Yahoo Finance library to aggregate real-time market data for the specified stock, such as current price, beta, earnings per share
        To specify which stock your want to research, add the stock ticker to the stockList array in the 'stockList.py' file
        Once sucessfully run, a cvs file called 'stock-analysis-{current date}' will downloaded in the folder.
        Open the file to view the data.

    get_news.py Script
        Leverages the Yahoo Finance library to aggregate news on specified stocks.
        To specify the stock you want the news for, add the stock ticker to the stockNewsList array in the 'stockList.py' file
        Once sucessfully run, a cvs file called 'stock-news-{current date}' will downloaded in the folder.
        Open the file to view the news.

    create



**Disclaimer**:
    Please do your own research and consult with a financial advisor before making any investment.
    This is only a personal project that I'm using the learn about automation and data analysis using python


