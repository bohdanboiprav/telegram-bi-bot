# This script contains the functions to scrape data from various websites and insert it into the database.
import asyncio
import aiocron
import json
import requests
from bs4 import BeautifulSoup
from database.db import async_insert


# Function to get the covid cases data from the worldometers website and insert it into the database
async def covid_cases_data():
    data_request = requests.get('https://www.worldometers.info/coronavirus/') # Requesting the data from the website
    soup = BeautifulSoup(data_request.content, 'html.parser') # Parsing the data using BeautifulSoup
    data_out = soup.find_all('div', class_='maincounter-number') # Finding the required data
    data_out = [int(data_out.find('span').text.strip().replace(',', '')) for data_out in data_out] # Cleaning the data
    await async_insert(
        f"INSERT INTO covid_cases (cases, deaths, recovered) VALUES ({data_out[0]}, {data_out[1]}, {data_out[2]})") # Inserting the data into the database
    print(f'{data_out[0]}, {data_out[1]}, {data_out[2]}')


# Mapping the stock names with their respective links
stock_mapping_dict = {
    'TSLA': 'https://finance.yahoo.com/quote/TSLA?.tsrc=fin-srch',
    'AMZN': 'https://finance.yahoo.com/quote/AMZN?.tsrc=fin-srch',
    'GOOGL': 'https://finance.yahoo.com/quote/GOOGL?.tsrc=fin-srch',
    'AAPL': 'https://finance.yahoo.com/quote/AAPL?.tsrc=fin-srch',
    'MSFT': 'https://finance.yahoo.com/quote/MSFT?.tsrc=fin-srch'
}

# Function to get the stock price data from the yahoo finance website and insert it into the database
async def get_stock_price(stock_name: str, stock_link: str): # Function to get the stock price data
    data_request = requests.get(stock_link) # Requesting the data from the website
    soup = BeautifulSoup(data_request.content, 'html.parser') # Parsing the data using BeautifulSoup
    stock_price = soup.find('div', class_='D(ib) Mend(20px)').find('fin-streamer').text.strip() # Finding the required data
    day_range = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[4].text.strip()
    pe_ratio = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[10].text.strip()
    week_range = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[5].text.strip()
    await async_insert(
        f"INSERT INTO stock_data (company, stock_price, day_range, pe_ratio, week_range) VALUES ('{stock_name}', '{stock_price}', '{day_range}', '{pe_ratio}', '{week_range}')") # Inserting the data into the database
    print(f"{stock_name}: {stock_price}\n📈Day Range: {day_range}\n📊PE Ratio: {pe_ratio}\n📉52 Week Range: {week_range}")


# Mapping the crypto names with their respective links
crypto_mapping_dict = {
    'BTCUSD': 'https://finance.yahoo.com/quote/BTC-USD',
    'ETHUSD': 'https://finance.yahoo.com/quote/ETH-USD',
    'XRPUSD': 'https://finance.yahoo.com/quote/XRP-USD',
    'SOLUSD': 'https://finance.yahoo.com/quote/SOL-USD',
    'DOGEUSD': 'https://finance.yahoo.com/quote/DOGE-USD'
}

# Function to get the crypto price data from the yahoo finance website and insert it into the database
async def get_crypto_price(crypto_name: str, crypto_link: str) -> None: # Function to get the crypto price data
    data_request = requests.get(crypto_link) # Requesting the data from the website
    soup = BeautifulSoup(data_request.content, 'html.parser') # Parsing the data using BeautifulSoup
    crypto_price = soup.find('div', class_='D(ib) Va(m) Maw(65%) Ov(h)').find("fin-streamer",
                                                                              class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").text.strip().replace(
        ',', '') # Finding the required data
    week_range = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[3].text.strip()
    price_increase = soup.find('div', class_='D(ib) Mend(20px)').find("fin-streamer",
                                                                      class_="Fw(500) Pstart(8px) Fz(24px)").text.strip().replace(
        ',', '')
    await async_insert(
        f"INSERT INTO crypto_data (crypto_name, crypto_price, week_range, price_increase) VALUES ('{crypto_name}', '{crypto_price}', '{week_range}', '{price_increase}')") # Inserting the data into the database
    print(
        f"{crypto_name}: {crypto_price}\n📊Week Range: {week_range}\n📈Price Increase: {price_increase}")


# Mapping the country names with their respective links
country_economy_mapping_dict = {
    '🇮🇪Ireland GDP': 'https://www.theglobaleconomy.com/Ireland/',
    '🇺🇸USA GDP': 'https://www.theglobaleconomy.com/USA/',
    '🇬🇧UK GDP': 'https://www.theglobaleconomy.com/United-Kingdom/',
    '🇲🇩Moldova GDP': 'https://www.theglobaleconomy.com/Moldova/',
    '🇺🇦Ukraine GDP': 'https://www.theglobaleconomy.com/Ukraine/'
}

# Function to get the country economic data from the theglobaleconomy website and insert it into the database
async def get_country_economic_data(country_name: str, country_link: str): # Function to get the country economic data
    data_request = requests.get(country_link) # Requesting the data from the website
    soup = BeautifulSoup(data_request.content, 'html.parser') # Parsing the data using BeautifulSoup
    real_gdp_percent = soup.find('div', class_='indicatorsLastValue mo re850px').text.strip() # Finding the required data
    inflation_cpi_percent = soup.find_all('div', class_='indicatorsLastValue mo re850px')[1].text.strip()
    unemployment_rate_percent = soup.find_all('div', class_='indicatorsLastValue mo re850px')[2].text.strip()
    await async_insert(
        f"INSERT INTO country_economy (country_name, real_gdp_percent, inflation_cpi_percent, unemployment_rate_percent) VALUES ('{country_name}', '{real_gdp_percent}', '{inflation_cpi_percent}', '{unemployment_rate_percent}')") # Inserting the data into the database
    print(
        f"{country_name}: {real_gdp_percent}\n📈Inflation CPI: {inflation_cpi_percent}\n📉Unemployment Rate: {unemployment_rate_percent}")


# @aiocron.crontab('* * * * *'), the function will run every minute
@aiocron.crontab('0 6 * * *') # Scheduling the function to run at 6:00 AM
async def scheduled_covid(): # Function to schedule the covid cases data
    await covid_cases_data() # Calling the function to get the covid cases data


@aiocron.crontab('4 5 * * *') # Scheduling the function to run at 5:04 AM
async def scheduled_stock(): # Function to schedule the stock price data
    for key, value in stock_mapping_dict.items(): # Looping through the stock mapping dictionary
        await get_stock_price(key, value) # Calling the function to get the stock price data


@aiocron.crontab('4 6 * * *') # Scheduling the function to run at 6:04 AM
async def scheduled_crypto(): # Function to schedule the crypto price data
    for key, value in crypto_mapping_dict.items(): # Looping through the crypto mapping dictionary
        await get_crypto_price(key, value) # Calling the function to get the crypto price data


@aiocron.crontab('0 7 * * *') # Scheduling the function to run at 7:00 AM
async def scheduled_country_economy(): # Function to schedule the country economic data
    for key, value in country_economy_mapping_dict.items(): # Looping through the country economy mapping dictionary
        await get_country_economic_data(key, value) # Calling the function to get the country economic data


"""In this script, we have defined functions to get the covid cases data, stock price data, crypto price data, 
and country economic data from the respective websites. We have also scheduled these functions to run at specific 
times using the aiocron library. The data is then inserted into the database using the async_insert function from 
the database.db module.) """
