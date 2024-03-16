from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class EconomyCallback(CallbackData, prefix="economy_tracker"):
    country: str
    real_gdp_percent: float
    inflation_cpi_percent: str
    unemployment_rate_percent: str


class EconomyCallbackReturn(CallbackData, prefix="economy_main"):
    text: str


def get_keyboard_economy(list_of_stocks: list):
    builder = InlineKeyboardBuilder()
    for i in list_of_stocks:
        builder.button(
            text=i[0], callback_data=EconomyCallback(country=i[0], real_gdp_percent=i[1], inflation_cpi_percent=i[2],
                                                     unemployment_rate_percent=i[3])
        )
    builder.adjust(3)
    return builder.as_markup()


def get_keyboard_economy_return():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙Back", callback_data=EconomyCallbackReturn(text="return"))
    builder.adjust(1)
    return builder.as_markup()
