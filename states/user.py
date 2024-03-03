from aiogram.fsm.state import (
    StatesGroup, State
)


class PageState(StatesGroup):
    start = State()
    add_user = State()
