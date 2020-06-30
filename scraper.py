import requests
from bs4 import BeautifulSoup

startDate = input("Start Date: ")
endDate = input("End Date: ")
 # Convert dates into Epoch


ticker = input("Ticker: ")
URL = 'https://finance.yahoo.com/quote/{Ticker}/history?period1={startEpoch}&period2={endEpoch}&interval=1d&filter=history&frequency=1d'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='')

for result in results:
