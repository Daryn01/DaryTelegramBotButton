from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
menu = ReplyKeyboardMarkup(
    Keyboard=[
        [
            KeyboardButton(text="2E"),
        ],
        [
            KeyboardButton(text="2E"),
            KeyboardButton(text="2E")
        ],
    ],
    resize_keyboard=True
)