# This file contains the keyboards for the economy tracker
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Callback data for the economy tracker
class OtherCallback(CallbackData, prefix="other_tracker"):
    action: str


# Callback data for the economy tracker return button
class OtherCallbackReturn(CallbackData, prefix="other_main"):
    text: str


# Function to get the keyboard for the economy tracker
def get_keyboard_other():
    builder = InlineKeyboardBuilder()
    builder.button(text="Covid Cases", callback_data=OtherCallback(action="covid_cases"))
    # builder.button(text="Other", callback_data=OtherCallback(text="back"))
    # builder.button(text="Other", callback_data=OtherCallback(text="back"))
    builder.adjust(1)
    return builder.as_markup()


# Function to get the return button for the economy tracker
def get_keyboard_other_return():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙Back", callback_data=OtherCallbackReturn(text="back"))
    builder.adjust(1)
    return builder.as_markup()


""""In the above code snippet, we have defined two CallbackData classes, OtherCallback and OtherCallbackReturn, to handle the
callback data for the other tracker and the return button. The get_keyboard_other function generates the keyboard for the
other tracker. The get_keyboard_other_return function generates the return button for the other tracker. These functions are
used in the handlers/other.py script to create the interactive keyboard for the other tracker."""
