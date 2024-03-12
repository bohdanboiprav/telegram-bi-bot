from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class CryptoCallback(CallbackData, prefix="crypto_tracker"):
    crypto: str
    crypto_price: float
    week_range: str
    price_increase: str


class CryptoCallbackReturn(CallbackData, prefix="crypto_main"):
    text: str


def get_keyboard_crypto(list_of_stocks: list):
    builder = InlineKeyboardBuilder()
    for i in list_of_stocks:
        builder.button(
            text=i[0], callback_data=CryptoCallback(crypto=i[0], crypto_price=i[1], week_range=i[2],
                                                    price_increase=i[3])
        )
    builder.adjust(3)
    return builder.as_markup()


def get_keyboard_crypto_return():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙Back", callback_data=CryptoCallbackReturn(text="return"))
    builder.adjust(1)
    return builder.as_markup()
