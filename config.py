# config.py

from aiogram import Bot, Dispatcher
from decouple import config

Admins = [5576961334, ]

token = config("TOKEN")

bot = Bot(token = token)
dp = Dispatcher(bot)