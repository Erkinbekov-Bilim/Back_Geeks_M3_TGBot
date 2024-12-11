# quiz.py

from aiogram import types, Dispatcher
from  aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyexpat.errors import messages

from config import bot
import os

async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)

    button = InlineKeyboardButton("Далее", callback_data='quiz_2')

    keyboard.add(button)

    question = 'XBOX or Sony'
    answer = ['XBOX', 'Sony', 'Nintendo']

    await bot.send_poll(
        chat_id = message.from_user.id, # Куда отправить опрос
        question = question,     # Сам вопрос
        options = answer,        # Варианты ответов
        is_anonymous = False,    # Анонимный или нет
        type = "quiz",           # Тип опросника
        correct_option_id = 1,   # id правильного ответа
        explanation = 'Жаль...', # Текст при неправильном ответе
        open_period = 60,        # Время работы опросника
        reply_markup=keyboard    # Добавление кнопки
    )

async def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)

    button = InlineKeyboardButton("Далее", callback_data='quiz_3')
    keyboard.add(button)

    question = 'Python, JavaScripts, Java, PHP and Swift'

    answer = ['Python', 'JavaScripts', 'Java', 'PHP', 'Swift']

    await bot.send_poll(
        chat_id = call.from_user.id, # Куда отправить опрос
        question = question,     # Сам вопрос
        options = answer,        # Варианты ответов
        is_anonymous = True,    # Анонимный или нет
        type = "quiz",           # Тип опросника
        correct_option_id = 0,   # id правильного ответа
        explanation = 'Всё с тобой понятно -_-', # Текст при неправильном ответе
        open_period = 180,
        reply_markup=keyboard
    )

async def quiz_3(call: types.CallbackQuery):
    question = "Кто изображен на картинке?"

    answer = ['Шрек', 'Кот в сапогах', 'Осел', 'Гоблин']

    photo_path = os.path.join('media', 'img.png')
    with open(photo_path, 'rb') as photo:
        await bot.send_photo(chat_id=call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        explanation='Правильный ответ - Шрек',
        open_period=30
    )

def register_quiz_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='quiz_2')
    dp.register_callback_query_handler(quiz_3, text='quiz_3')

