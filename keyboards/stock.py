from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class StockCallback(CallbackData, prefix="stock_tracker"):
    company: str
    stock_price: float
    day_range: str
    pe_ratio: float
    week_range: str


class StockCallbackReturn(CallbackData, prefix="stock_main"):
    text: str


def get_keyboard_stock(list_of_stocks: list):
    builder = InlineKeyboardBuilder()
    for i in list_of_stocks:
        builder.button(
            text=i[0], callback_data=StockCallback(company=i[0], stock_price=i[1], day_range=i[2], pe_ratio=i[3],
                                                   week_range=i[4])
        )
    builder.adjust(3)
    return builder.as_markup()


def get_keyboard_stock_return():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙Back", callback_data=StockCallbackReturn(text="covid_cases"))
    builder.adjust(1)
    return builder.as_markup()
