import requests
from bs4 import BeautifulSoup

data_request = requests.get('https://finance.yahoo.com/quote/TSLA?.tsrc=fin-srch')
soup = BeautifulSoup(data_request.content, 'html.parser')
stock_price = soup.find('div', class_='D(ib) Mend(20px)').find('fin-streamer').text.strip()
day_range = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[4].text.strip()
pe_ratio = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[10].text.strip()
week_range = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[5].text.strip()
print(stock_price, day_range, pe_ratio, week_range)
