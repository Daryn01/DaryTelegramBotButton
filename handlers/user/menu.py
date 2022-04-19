from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu

@pdp.message_handler(Command("start"))
async def show_menu(message:Message):
    await message.answer("Choose one", reply_markup=menu)

@dp.message_handler(Text(equals=["2E","4E","3I"]))
async def get_food(message:Message):
    await message.answer(f"Choosen {message.text}. Thanks",
                         reply_markup=ReplyKeyboardRemove())