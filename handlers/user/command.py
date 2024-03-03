from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from filters.__main__ import MessageFilter
from keyboards.user import HOME_KEYBOARD
from messages.user import Messages
from models.user import User
from utils.db import session

router: Router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    user = User(tg_id=message.from_user.id, first_name=message.from_user.first_name)
    session.add(user)
    session.commit()
    await message.answer(str(Messages.start), reply_markup=HOME_KEYBOARD)


@router.message(MessageFilter("salom"))
async def message_handler(message: Message):
    await message.answer("salom")
