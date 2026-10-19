import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

from buttons import main_menu, Kurslar

bot = Bot(token="8651654192:AAE1mgOFChPshjAhW--rgkJ1PI0vQ2sdSYU")
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    full_name = message.from_user.full_name
    await message.answer(f"Assalomu Alekum {full_name} ", reply_markup=await main_menu()) 



@dp.message(F.text == "Kurslar")
async def reaction_to_Kurslar(message: Message):
    await message.answer(f"Bittasini tanlang!", reply_markup= await Kurslar())



@dp.callback_query(F.data == "course_python")
async def call_course_info(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Python haqida malumot. Davomiyligi: 5 oy. Oylik Tolov: 800 min dan")

@dp.callback_query(F.data == "course_web")
async def call_course_info(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Web Dasturlash haqida malumot. Davomiyligi: 10 oy. Oylik Tolov: 1400 mln dan")


@dp.callback_query(F.data == "course_frontend")
async def call_course_info(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Frontend  haqida malumot. Davomiyligi: 8 oy. Oylik Tolov: 1 mln dan")


@dp.callback_query(F.data == "course_dizayn")
async def call_course_info(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Grafik dizayn haqida malumot. Davomiyligi: 7 oy. Oylik Tolov: 700 min dan")





async def main():
    await dp.start_polling(bot)

asyncio.run(main())