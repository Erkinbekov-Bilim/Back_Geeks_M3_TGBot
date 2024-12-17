# echo.py

from aiogram import types, Dispatcher
import random


async def echo_handler(message: types.Message):
    games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
    text = message.text

    if text.isdigit():
        text_to_number = int(text) * 2
        await message.answer(text=str(text_to_number))
    elif text == "game":
        await message.answer_dice(random.choice(games))
    elif text != 'game':
        await message.answer(text=text)




def register_echo_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_handler)
