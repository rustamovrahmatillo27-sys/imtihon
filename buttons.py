
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def main_menu():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Kurslar"),
                KeyboardButton(text="Kursga yozilish")
            ],
            [
                KeyboardButton(text="Markaz haqida"),
                KeyboardButton(text="Aloqa")
            ]
        ],
        resize_keyboard=True
    )
    return markup


async def Kurslar():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Python",callback_data="course_python")
            ],
            [
                InlineKeyboardButton(text="Web dasturlash",callback_data="course_web")
            ],
            [
                InlineKeyboardButton(text="Frontend",callback_data="course_frontend")
            ],
            [
                InlineKeyboardButton(text="Grafik dizayn",callback_data="course_dizayn")
            ]
        ]
    )
    return markup