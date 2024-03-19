# This file contains the keyboard for the crypto tracker
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Callback data for the crypto tracker
class CryptoCallback(CallbackData, prefix="crypto_tracker"):
    crypto: str
    crypto_price: float
    week_range: str
    price_increase: str


# Callback data for the crypto tracker return button
class CryptoCallbackReturn(CallbackData, prefix="crypto_main"):
    text: str


# Function to get the keyboard for the crypto tracker
def get_keyboard_crypto(list_of_stocks: list):
    builder = InlineKeyboardBuilder()
    for i in list_of_stocks:
        builder.button(
            text=i[0], callback_data=CryptoCallback(crypto=i[0], crypto_price=i[1], week_range=i[2],
                                                    price_increase=i[3])
        )
    builder.adjust(3)
    return builder.as_markup()


# Function to get the return button for the crypto tracker
def get_keyboard_crypto_return():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙Back", callback_data=CryptoCallbackReturn(text="return"))
    builder.adjust(1)
    return builder.as_markup()


"""In the above code snippet, we have defined two CallbackData classes, CryptoCallback and CryptoCallbackReturn, to handle the
callback data for the crypto tracker and the return button. The get_keyboard_crypto function generates the keyboard for the
crypto tracker based on the list of stocks provided. The get_keyboard_crypto_return function generates the return button for
the crypto tracker. These functions are used in the handlers/crypto.py script to create the interactive keyboard for the
crypto tracker."""
