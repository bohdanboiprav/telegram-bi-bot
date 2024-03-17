from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class OtherCallback(CallbackData, prefix="other_tracker"):
    action: str


class OtherCallbackReturn(CallbackData, prefix="other_main"):
    text: str


def get_keyboard_other():
    builder = InlineKeyboardBuilder()
    builder.button(text="Covid Cases", callback_data=OtherCallback(action="covid_cases"))
    # builder.button(text="Other", callback_data=OtherCallback(text="back"))
    # builder.button(text="Other", callback_data=OtherCallback(text="back"))
    builder.adjust(1)
    return builder.as_markup()


def get_keyboard_other_return():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙Back", callback_data=OtherCallbackReturn(text="back"))
    builder.adjust(1)
    return builder.as_markup()
