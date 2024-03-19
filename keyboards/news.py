from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Callback data for the news tracker
class NewsCallback(CallbackData, prefix="news_tracker"):
    action: str


# Callback data for the news tracker return button
class OtherCallbackReturn(CallbackData, prefix="other_main"):
    text: str


# Function to get the keyboard for the news tracker
def get_keyboard_other():
    builder = InlineKeyboardBuilder()
    builder.button(text="Covid Cases", callback_data=NewsCallback(action="covid_cases"))
    builder.adjust(1)
    return builder.as_markup()


# Function to get the return button for the news tracker
def get_keyboard_other_return():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙Back", callback_data=OtherCallbackReturn(text="back"))
    builder.adjust(1)
    return builder.as_markup()


"""In the above code snippet, we have defined two CallbackData classes, NewsCallback and OtherCallbackReturn, to handle the
callback data for the news tracker and the return button. The get_keyboard_other function generates the keyboard for the
news tracker. The get_keyboard_other_return function generates the return button for the news tracker. These functions are
used in the handlers/news.py script to create the interactive keyboard for the news tracker."""
