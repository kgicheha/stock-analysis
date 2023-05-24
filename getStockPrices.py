import requests
from bs4 import BeautifulSoup



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
# url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'
url = 'https://finance.yahoo.com/quote/AAPL'
response = requests.get(url, headers=headers)
# print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title.text)
price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})["value"]

print(price)

