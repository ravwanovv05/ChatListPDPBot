from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def m_buttons():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text='Taklif/Shikoyat'))
    builder.add(KeyboardButton(text='PDP Academy gurhlari va botlari'))

    return builder.as_markup(resize_keyboard=True)


