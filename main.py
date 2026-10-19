import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from buttons import main_menu, Kurslar
from state import Register



bot = Bot(token="8651654192:AAE1mgOFChPshjAhW--rgkJ1PI0vQ2sdSYU")
dp = Dispatcher()



@dp.message(CommandStart())
async def start(message: Message):
    full_name = message.from_user.full_name
    await message.answer(f"Assalomu alaykum, {full_name}", reply_markup=await main_menu())



@dp.message(F.text == "Kurslar")
async def reaction_to_Kurslar(message: Message):
    await message.answer("Bittasini tanlang!", reply_markup=await Kurslar())



@dp.message(F.text == "Kursga yozilish")
async def register(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Ismingizni kiriting:")
    await state.set_state(Register.name)



@dp.message(Register.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name= message.text)
    await message.answer("Telefon raqamingizni kiriting:")
    await state.set_state(Register.phone)



@dp.message(Register.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Kursni tanlang:", reply_markup=await Kurslar())
    await state.set_state(Register.course)


@dp.callback_query(Register.course,F.data.in_(["course_python","course_web","course_frontend","course_dizayn" ]))

async def get_course(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    courses = {
        "course_python": "Python",
        "course_web": "Web dasturlash",
        "course_frontend": "Frontend",
        "course_dizayn": "Grafik dizayn"
    }
    data = await state.get_data()
    await callback.message.answer(f"Malumotlaringiz:\n"f"Ism: {data['name']}\n" f"Telefon: {data['phone']}\n" f"Kurs: {courses[callback.data]}\n" f"Kursga yozildingiz!")
    await state.clear()



@dp.callback_query(F.data == "course_python")
async def call_course_python(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Python haqida ma'lumot.\n" "Davomiyligi: 5 oy.\n" "Oylik to'lov: 800 ming so'mdan.")



@dp.callback_query(F.data == "course_web")
async def call_course_web(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Web dasturlash haqida ma'lumot.\n" "Davomiyligi: 10 oy.\n" "Oylik to'lov: 1 mln 400 ming so'mdan.")



@dp.callback_query(F.data == "course_frontend")
async def call_course_frontend(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Frontend haqida ma'lumot.\n" "Davomiyligi: 8 oy.\n" "Oylik to'lov: 1 mln so'mdan.")



@dp.callback_query(F.data == "course_dizayn")
async def call_course_dizayn(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Grafik dizayn haqida ma'lumot.\n" "Davomiyligi: 7 oy.\n" "Oylik to'lov: 700 ming so'mdan.")



@dp.message(F.text == "Markaz haqida")
async def markaz(message: Message):
    await message.answer("O'quv markazimizda IT kurslari bor")



@dp.message(F.text == "Aloqa")
async def aloqa(message: Message):
    await message.answer("Telefon: +998 50 711 04 86\n""Manzil: Margilon")


@dp.message(Command("cancel"))
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Ro'yxatdan o'tish bekor qilindi.", reply_markup=await main_menu())



async def main():
    await dp.start_polling(bot)

asyncio.run(main())