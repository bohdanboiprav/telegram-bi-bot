import asyncio
import logging
import datetime
import sys
from random import randint

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart, Command

from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold
from aiogram import F

from conf.config import settings

from database.db import async_select_one, async_select_all
from keyboards.crypto import CryptoCallback, CryptoCallbackReturn, get_keyboard_crypto, get_keyboard_crypto_return
from keyboards.economy import EconomyCallbackReturn, get_keyboard_economy, EconomyCallback, get_keyboard_economy_return
from keyboards.other import get_keyboard_other, OtherCallback, get_keyboard_other_return, OtherCallbackReturn
from keyboards.stock import get_keyboard_stock, get_keyboard_stock_return, StockCallback, StockCallbackReturn
from services.news_api import get_news

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"""👋Hello, {hbold(message.from_user.full_name)}!
    I’m your Business Analytics Assistant Bot, designed to empower your decision-making with real-time insights and data-driven clarity. Here’s what I can do:

📈 Stock Information: Get real-time stock data on your favourite stocks using professional metrics.
📰 Financial News and Insights: Stay informed with the top latest financial news.
💰 Cryptocurrency Price Tracker: Monitor crypto prices in real-time using professional metrics.
🌐 Other Trackers: Track data about COVID, WORLD POPULATION, GOVERNMENT & ECONOMICS.
❓ Struggling? Just use the help button to unlock the insights of the Business Analytics Assistant Bot.

I fetch real-time data from reliable financial APIs, scrape articles from reputable financial sources. Your data’s privacy and security are my top priority. Let me assist you in your data-driven journey! 🚀📈""")


@dp.message(Command("stock_tracker"))
async def command_start_handler(message: Message) -> None:
    query = """SELECT *
                FROM stock_data
                WHERE DATE_TRUNC('minutes', report_timestamp) = (SELECT MAX(DATE_TRUNC('minutes', report_timestamp)) FROM stock_data)
            """
    global stock_data
    stock_data = await async_select_all(query)

    await message.answer("""Use the buttons below to check the stock prices.""",
                         reply_markup=get_keyboard_stock([x[2:] for x in stock_data]))


@dp.callback_query(StockCallback.filter())
async def stock_callback(query: CallbackQuery, callback_data: StockCallback):
    await query.message.edit_text(
        f"{callback_data.company}: {callback_data.stock_price}\n📈Day Range: {callback_data.day_range}\n📊PE Ratio: {callback_data.pe_ratio}\n📉52 Week Range: {callback_data.week_range}",
        reply_markup=get_keyboard_stock_return())


@dp.callback_query(StockCallbackReturn.filter())
async def stock_callback_return(query: CallbackQuery, callback_data: StockCallbackReturn):
    if stock_data:
        await query.message.edit_text("""Use the buttons below to check the stock prices.""",
                                      reply_markup=get_keyboard_stock([x[2:] for x in stock_data]))
    else:
        await query.message.edit_text("No stock data found")


@dp.message(Command("crypto_tracker"))
async def command_crypto_handler(message: Message) -> None:
    query = """SELECT *
                FROM crypto_data
                WHERE DATE_TRUNC('minutes', report_timestamp) = (SELECT MAX(DATE_TRUNC('minutes', report_timestamp)) FROM crypto_data)
            """
    global crypto_data
    crypto_data = await async_select_all(query)

    await message.answer("""Use the buttons below to check the crypto prices.""",
                         reply_markup=get_keyboard_crypto([x[2:] for x in crypto_data]))


@dp.callback_query(CryptoCallback.filter())
async def crypto_callback(query: CallbackQuery, callback_data: CryptoCallback):
    await query.message.edit_text(
        f"{callback_data.crypto}: {callback_data.crypto_price}\n📈Week Range: {callback_data.week_range}\n📊Price Increase: {callback_data.price_increase}",
        reply_markup=get_keyboard_crypto_return())


@dp.callback_query(CryptoCallbackReturn.filter())
async def crypto_callback_return(query: CallbackQuery, callback_data: CryptoCallbackReturn):
    if crypto_data:
        await query.message.edit_text("""Use the buttons below to check the crypto prices.""",
                                      reply_markup=get_keyboard_crypto([x[2:] for x in crypto_data]))
    else:
        await query.message.edit_text("No crypto data found")


@dp.message(Command("gdp_tracker"))
async def command_economy_handler(message: Message) -> None:
    query = """SELECT *
                FROM country_economy
                WHERE DATE_TRUNC('minutes', report_timestamp) = (SELECT MAX(DATE_TRUNC('minutes', report_timestamp)) FROM country_economy)
            """
    global economy_data
    economy_data = await async_select_all(query)

    await message.answer("""Use the buttons below to check the GDP data for your country.""",
                         reply_markup=get_keyboard_economy([x[2:] for x in economy_data]))


@dp.callback_query(EconomyCallback.filter())
async def economy_callback(query: CallbackQuery, callback_data: EconomyCallback):
    await query.message.edit_text(
        f"{callback_data.country}: {callback_data.real_gdp_percent}\n📈Inflation CPI: {callback_data.inflation_cpi_percent}\n📉Unemployment Rate: {callback_data.unemployment_rate_percent}",
        reply_markup=get_keyboard_economy_return())


@dp.callback_query(EconomyCallbackReturn.filter())
async def economy_callback_return(query: CallbackQuery, callback_data: EconomyCallbackReturn):
    if economy_data:
        await query.message.edit_text("""Use the buttons below to check the GDP data for your country.""",
                                      reply_markup=get_keyboard_economy([x[2:] for x in economy_data]))
    else:
        await query.message.edit_text("No gdp data found")


@dp.message(Command("other_trackers"))
async def other_handler(message: types.Message) -> None:
    await message.answer("Please select want information you want to get", reply_markup=get_keyboard_other())


@dp.callback_query(OtherCallback.filter())
async def other_callback(query: CallbackQuery, callback_data: OtherCallback):
    if callback_data.action == "covid_cases":
        sql_query = """SELECT
                    report_date,
                    cases - LAG(cases, 1, 0) OVER (ORDER BY report_date) AS daily_cases,
                    deaths - LAG(deaths, 1, 0) OVER (ORDER BY report_date) AS daily_deaths,
                    recovered - LAG(recovered, 1, 0) OVER (ORDER BY report_date) AS daily_recovered
                    FROM covid_cases
                    ORDER BY report_date desc
                    limit 1"""
        cases = await async_select_one(sql_query)
        reply_string = f"COVID-19 Data on {cases[0]}\n🦠Cases: {cases[1]}\n☠️Deaths: {cases[2]}\n🏥Recovered: {cases[3]}"
        await query.message.edit_text(reply_string, reply_markup=get_keyboard_other_return())


@dp.callback_query(OtherCallbackReturn.filter())
async def stock_callback_return(query: CallbackQuery, callback_data: OtherCallbackReturn):
    await query.message.edit_text("Please select want information you want to get", reply_markup=get_keyboard_other())


@dp.message(Command("news_tracker"))
async def other_handler(message: types.Message) -> None:
    kb = [
        [
            types.KeyboardButton(text="1 news"),
            types.KeyboardButton(text="3 news"),
            types.KeyboardButton(text="5 news"),
            types.KeyboardButton(text="10 news")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Delete news from chat"
    )
    await message.answer("Please select number of news", reply_markup=keyboard)


@dp.message(F.text.lower() == '1 news')
async def news_handler(message: types.Message):
    news_data = get_news(1)
    for i in news_data:
        await message.answer_photo(photo=i['url'],
                                   caption=f"{i['title']}\n\n{i['description'] if i['description'] else ''}\n\nRead more:\n{i['url']}\n\n",
                                   reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text.lower() == '3 news')
async def news_handler(message: types.Message):
    news_data = get_news(3)
    for i in news_data:
        await message.answer_photo(photo=i['url'],
                                   caption=f"{i['title']}\n\n{i['description'] if i['description'] else ''}\n\nRead more:\n{i['url']}\n\n",
                                   reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text.lower() == '5 news')
async def news_handler(message: types.Message):
    news_data = get_news(5)
    for i in news_data:
        await message.answer_photo(photo=i['url'],
                                   caption=f"{i['title']}\n\n{i['description'] if i['description'] else ''}\n\nRead more:\n{i['url']}\n\n",
                                   reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.text.lower() == '10 news')
async def news_handler(message: types.Message):
    news_data = get_news(10)
    for i in news_data:
        await message.answer_photo(photo=i['url'],
                                   caption=f"{i['title']}\n\n{i['description'] if i['description'] else ''}\n\nRead more:\n{i['url']}\n\n",
                                   reply_markup=types.ReplyKeyboardRemove())


@dp.message(Command("help"))
async def news_handler(message: types.Message) -> None:
    await message.answer("""Here is the list of commands you can use:\n\n 
    /start - To start the bot\n
    /stock_tracker - To get the stock prices\n
    /other_trackers - To get the other trackers list\n
    /help - To get the list of commands\n
    """)


@dp.message()
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"I'm not sure what you meant.\n\nPlease check the bot's description or use the '/help' command to see its available functionalities and commands")
