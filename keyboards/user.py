from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Keyboards:
    def __init__(self):
        self.HOME_KEYBOARD = ReplyKeyboardMarkup(keyboard=[
            [
                KeyboardButton(text="salom")
            ]
        ], resize_keyboard=True)
