import asyncio
import logging
import sys

from aiogram.utils.i18n import I18n

from bot import dp, bot
from middlewares.__main__ import BotI18nMiddleware
from utils.__main__ import import_handlers, import_db, import_module


async def main() -> None:
    i18n = I18n(path="locales", default_locale="en")
    dp.message.middleware.register(BotI18nMiddleware(i18n))

    await import_handlers()
    await import_module("models")
    await import_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
