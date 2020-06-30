import requests
from bs4 import BeautifulSoup
import datetime
import time

d= input('Enter a date in YYYY-MM-DD format') + ' 00:00:00'
p='%Y-%m-%d %H:%M:%S'
startEpoch = int(time.mktime(time.strptime(d,p)))
endEpoch = startEpoch + 1209600
ticker = input("Ticker: ").upper()


URL = f'https://finance.yahoo.com/quote/{ticker}/history?period1={startEpoch}&period2={endEpoch}&interval=1d&filter=history&frequency=1d'
page = requests.get(URL)
print(URL)
html_doc = """<table class="W(100%) M(0)" data-test="historical-prices">"""
soup = BeautifulSoup(html_doc, "html.parser")
# results = soup.find()


