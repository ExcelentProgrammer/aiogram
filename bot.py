from aiogram import Bot, Dispatcher, Router

from utils.env import env

bot = Bot(env.str("BOT_TOKEN"))

dp = Dispatcher()

