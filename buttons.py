from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardButton 

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



from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def Kurslar():
    markup=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Python", callback_data="course_python")],
        [InlineKeyboardButton(text="Web dasturlash", callback_data="course_web")],
        [InlineKeyboardButton(text="Frontend", callback_data="course_frontend")],
        [InlineKeyboardButton(text="Grafik dizayn", callback_data="course_dizayn")]
        
    ]
    )
    return markup


async def Kursga_yozilish(): 
 ReplyKeyboardMarkup
 return ReplyKeyboardMarkup(
       keyboard = [[ KeyboardButton(text = "Bekor qilish") ]],
       resize_keyboard = True,
message = "Ism-familiyangizni kiriting")

async def TelefonRaqam():
 ReplyKeyboardMarkup
 return ReplyKeyboardMarkup(
    keyboard = [
    [KeyboardButton(text = "Telefon raqamni yuborish", request_contact = True)],
    [KeyboardButton(text = "Bekor qilish")],
], 
    resize_keyboard = True,
    message = "Telefon raqamingizni kiriting"
)

async def KursTanlash():
 InlineKeyboardMarkup
 return InlineKeyboardMarkup(
inline_keyboard = [
    [InlineKeyboardButton(text = "Python", callback_data = "course_python")],
    [InlineKeyboardButton(text = "Web dasturlash", callback_data = "course_web")],
    [InlineKeyboardButton(text = "Frontend", callback_data = "course_frontend")],
    [InlineKeyboardButton(text = "Grafik dizayn", callback_data = "course_design")],
    [InlineKeyboardButton(text = "Bekor qilish", callback_data = "cancel_registration")]
])


