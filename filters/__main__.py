from aiogram.filters import BaseFilter
from aiogram.types import Message


class MessageFilter(BaseFilter):
    def __init__(self, text):
        self.text = text

    async def __call__(self, message: Message):
        return message.text == self.text
