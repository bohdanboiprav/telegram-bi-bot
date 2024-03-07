import asyncio
import json
import requests
from bs4 import BeautifulSoup

from database.db import async_insert


async def covid_cases_data():
    data_request = requests.get('https://www.worldometers.info/coronavirus/')
    soup = BeautifulSoup(data_request.content, 'html.parser')
    data_out = soup.find_all('div', class_='maincounter-number')
    data_out = [int(data_out.find('span').text.strip().replace(',', '')) for data_out in data_out]
    await async_insert(
        f"INSERT INTO covid_cases (cases, deaths, recovered) VALUES ({data_out[0]}, {data_out[1]}, {data_out[2]})")
    return f'{data_out[0]}, {data_out[1]}, {data_out[2]}'


stock_mapping_dict = {
    'TSLA': 'https://www.marketwatch.com/investing/stock/tsla',
    'AMZN': 'https://www.marketwatch.com/investing/stock/amzn',
    'GOOGL': 'https://www.marketwatch.com/investing/stock/googl',
    'AAPL': 'https://www.marketwatch.com/investing/stock/aapl',
    'MSFT': 'https://www.marketwatch.com/investing/stock/msft'
}


async def get_stock_price(stock_name: str, stock_link: str):
    data_request = requests.get(stock_link)
    soup = BeautifulSoup(data_request.content, 'html.parser')
    stock_price = float(soup.find('h2', class_='intraday__price').find('bg-quote', class_='value').text.strip())
    day_range = soup.find_all('span', class_='primary')[7].text.strip()
    pe_ratio = float(soup.find_all('span', class_='primary')[14].text.strip())
    week_range = soup.find_all('span', class_='primary')[8].text.strip()
    await async_insert(
        f"INSERT INTO stock_data (company, stock_price, day_range, pe_ratio, week_range) VALUES ('{stock_name}', '{stock_price}', '{day_range}', '{pe_ratio}', '{week_range}')")
    return f"{stock_name}: {stock_price}\n📈Day Range: {day_range}\n📊PE Ratio: {pe_ratio}\n📉52 Week Range: {week_range}"


for key, value in stock_mapping_dict.items():
    print(asyncio.run(get_stock_price(key, value)))
