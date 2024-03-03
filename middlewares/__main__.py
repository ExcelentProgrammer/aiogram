from typing import Any

from aiogram.utils.i18n import I18nMiddleware


class BotI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event, data: dict[str, Any]) -> str:
        return 'en'
