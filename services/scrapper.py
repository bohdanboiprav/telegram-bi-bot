import asyncio
import aiocron
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
    print(f'{data_out[0]}, {data_out[1]}, {data_out[2]}')


stock_mapping_dict = {
    'TSLA': 'https://finance.yahoo.com/quote/TSLA?.tsrc=fin-srch',
    'AMZN': 'https://finance.yahoo.com/quote/AMZN?.tsrc=fin-srch',
    'GOOGL': 'https://finance.yahoo.com/quote/GOOGL?.tsrc=fin-srch',
    'AAPL': 'https://finance.yahoo.com/quote/AAPL?.tsrc=fin-srch',
    'MSFT': 'https://finance.yahoo.com/quote/MSFT?.tsrc=fin-srch'
}


async def get_stock_price(stock_name: str, stock_link: str):
    data_request = requests.get(stock_link)
    soup = BeautifulSoup(data_request.content, 'html.parser')
    stock_price = soup.find('div', class_='D(ib) Mend(20px)').find('fin-streamer').text.strip()
    day_range = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[4].text.strip()
    pe_ratio = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[10].text.strip()
    week_range = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[5].text.strip()
    await async_insert(
        f"INSERT INTO stock_data (company, stock_price, day_range, pe_ratio, week_range) VALUES ('{stock_name}', '{stock_price}', '{day_range}', '{pe_ratio}', '{week_range}')")
    print(f"{stock_name}: {stock_price}\n📈Day Range: {day_range}\n📊PE Ratio: {pe_ratio}\n📉52 Week Range: {week_range}")


crypto_mapping_dict = {
    'BTCUSD': 'https://finance.yahoo.com/quote/BTC-USD',
    'ETHUSD': 'https://finance.yahoo.com/quote/ETH-USD',
    'XRPUSD': 'https://finance.yahoo.com/quote/XRP-USD',
    'SOLUSD': 'https://finance.yahoo.com/quote/SOL-USD',
    'DOGEUSD': 'https://finance.yahoo.com/quote/DOGE-USD'
}


async def get_crypto_price(crypto_name: str, crypto_link: str) -> None:
    data_request = requests.get(crypto_link)
    soup = BeautifulSoup(data_request.content, 'html.parser')
    crypto_price = soup.find('div', class_='D(ib) Va(m) Maw(65%) Ov(h)').find("fin-streamer",
                                                                              class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").text.strip().replace(
        ',', '')
    # day_range = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[2].text.strip()
    week_range = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[3].text.strip()
    price_increase = soup.find('div', class_='D(ib) Mend(20px)').find("fin-streamer",
                                                                      class_="Fw(500) Pstart(8px) Fz(24px)").text.strip().replace(
        ',', '')
    await async_insert(
        f"INSERT INTO crypto_data (crypto_name, crypto_price, week_range, price_increase) VALUES ('{crypto_name}', '{crypto_price}', '{week_range}', '{price_increase}')")
    print(
        f"{crypto_name}: {crypto_price}\n📊Week Range: {week_range}\n📈Price Increase: {price_increase}")


# for key, value in stock_mapping_dict.items():
#     print(asyncio.run(get_stock_price(key, value)))

# for key, value in crypto_mapping_dict.items():
#     print(asyncio.run(get_crypto_price(key, value)))

# @aiocron.crontab('* * * * *')
@aiocron.crontab('0 6 * * *')
async def scheduled_covid_and_stock():
    await covid_cases_data()
    for key, value in stock_mapping_dict.items():
        await get_stock_price(key, value)


# @aiocron.crontab('* * * * *')
@aiocron.crontab('0 6 * * *')
async def scheduled_crypto():
    for key, value in crypto_mapping_dict.items():
        await get_crypto_price(key, value)
