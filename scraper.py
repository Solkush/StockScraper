import requests, pandas, lxml
from lxml import html
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
element_html = html.fromstring(page.content)
table = element_html.xpath('//table')
table_tree = lxml.etree.tostring(table[0], method='xml')
panda = pandas.read_html(table_tree)
print(table_tree)


