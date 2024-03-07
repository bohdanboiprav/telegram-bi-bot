import requests
from bs4 import BeautifulSoup

data_request = requests.get('https://www.marketwatch.com/investing/stock/tsla')
soup = BeautifulSoup(data_request.content, 'html.parser')
stock_price = soup.find('h2', class_='intraday__price') #.find('bg-quote', class_='value').text.strip())
day_range = soup.find_all('span', class_='primary')[7].text.strip()
pe_ratio = float(soup.find_all('span', class_='primary')[14].text.strip())
week_range = soup.find_all('span', class_='primary')[8].text.strip()
print(stock_price, day_range, pe_ratio, week_range)
