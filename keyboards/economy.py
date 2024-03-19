# This file contains the keyboards for the economy tracker
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Callback data for the economy tracker
class EconomyCallback(CallbackData, prefix="economy_tracker"):
    country: str
    real_gdp_percent: float
    inflation_cpi_percent: str
    unemployment_rate_percent: str


# Callback data for the economy tracker return button
class EconomyCallbackReturn(CallbackData, prefix="economy_main"):
    text: str


# Function to get the keyboard for the economy tracker
def get_keyboard_economy(list_of_stocks: list):
    builder = InlineKeyboardBuilder()
    for i in list_of_stocks:
        builder.button(
            text=i[0], callback_data=EconomyCallback(country=i[0], real_gdp_percent=i[1], inflation_cpi_percent=i[2],
                                                     unemployment_rate_percent=i[3])
        )
    builder.adjust(3)
    return builder.as_markup()


# Function to get the return button for the economy tracker
def get_keyboard_economy_return():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙Back", callback_data=EconomyCallbackReturn(text="return"))
    builder.adjust(1)
    return builder.as_markup()


"""In the above code snippet, we have defined two CallbackData classes, EconomyCallback and EconomyCallbackReturn, to handle the
callback data for the economy tracker and the return button. The get_keyboard_economy function generates the keyboard for the
economy tracker based on the list of stocks provided. The get_keyboard_economy_return function generates the return button for
the economy tracker. These functions are used in the handlers/economy.py script to create the interactive keyboard for the
economy tracker."""
