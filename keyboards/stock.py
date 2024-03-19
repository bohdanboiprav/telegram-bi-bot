# This file contains the keyboard for the stock tracker
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Callback data for the stock tracker
class StockCallback(CallbackData, prefix="stock_tracker"):
    company: str
    stock_price: float
    day_range: str
    pe_ratio: float
    week_range: str


# Callback data for the stock tracker return button
class StockCallbackReturn(CallbackData, prefix="stock_main"):
    text: str


# Function to get the keyboard for the stock tracker
def get_keyboard_stock(list_of_stocks: list):
    builder = InlineKeyboardBuilder()
    for i in list_of_stocks:
        builder.button(
            text=i[0], callback_data=StockCallback(company=i[0], stock_price=i[1], day_range=i[2], pe_ratio=i[3],
                                                   week_range=i[4])
        )
    builder.adjust(3)
    return builder.as_markup()


# Function to get the return button for the stock tracker
def get_keyboard_stock_return():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙Back", callback_data=StockCallbackReturn(text="covid_cases"))
    builder.adjust(1)
    return builder.as_markup()


"""In the above code snippet, we have defined two CallbackData classes, StockCallback and StockCallbackReturn, to handle the
callback data for the stock tracker and the return button. The get_keyboard_stock function generates the keyboard for the
stock tracker based on the list of stocks provided. The get_keyboard_stock_return function generates the return button for
the stock tracker. These functions are used in the handlers/stock.py script to create the interactive keyboard for the
stock tracker."""
