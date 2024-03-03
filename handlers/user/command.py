from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from filters.__main__ import MessageFilter
from keyboards.user import HOME_KEYBOARD
from messages.user import Messages
from models.user import User
from states.user import PageState
from utils.db import session

router: Router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    user = User(tg_id=message.from_user.id, first_name=message.from_user.first_name)
    session.add(user)
    session.commit()
    await state.set_state(PageState.add_user)
    await message.answer(str(Messages.start), reply_markup=HOME_KEYBOARD)


@router.message(PageState.add_user)
async def add_user_handler(message: Message, state: FSMContext):
    await message.answer("ishladi")
    await state.set_state(PageState.start)


@router.message(MessageFilter("salom"))
async def message_handler(message: Message):
    await message.answer("salom")
