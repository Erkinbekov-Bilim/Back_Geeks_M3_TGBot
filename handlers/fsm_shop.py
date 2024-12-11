# fsm_shop.py

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from .fsm_reg import load_submit, cancel_fsm
from buttons import cancel_markup


class FSMShop(StatesGroup):
    name_model = State()
    Size_model = State()
    Category_model = State()
    Price_model = State()
    Photo_model = State()
    Submit_model = State()


async def start_fsm_shop(message: types.Message):
    await message.answer('Введите название модели:', reply_markup=cancel_markup)
    await FSMShop.name_model.set()


async def load_name_model(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name_model"] = message.text

    await FSMShop.next()
    await message.answer('Введите размер модели:')


async def load_size_model(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["size_model"] = message.text

    await FSMShop.next()
    await message.answer('Введите категорию модели:')


async def load_category_model(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["category_model"] = message.text

    await FSMShop.next()
    await message.answer('Введите цену модели:')

async def load_price_model(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["price_model"] = message.text

    await FSMShop.next()
    await message.answer('Отправьте фото модели:')

async def load_photo_model(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo_model"] = message.photo[-1].file_id

    await FSMShop.next()
    await message.answer(f'Верны ли данные?')
    await message.answer_photo(photo=data["photo_model"],
                               caption=f'Название модели - {data["name_model"]}\n'
                               f'Размер модели - {data["size_model"]}\n'
                               f'Категория модели - {data["category_model"]}\n'
                               f'Цена модели - {data["price_model"]}')


def register_handlers_fsm_shop(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals="cancel", ignore_case=True), state="*")

    dp.register_message_handler(start_fsm_shop, commands=['shop'], state=None)
    dp.register_message_handler(load_name_model, state=FSMShop.name_model)
    dp.register_message_handler(load_size_model, state=FSMShop.Size_model)
    dp.register_message_handler(load_category_model, state=FSMShop.Category_model)
    dp.register_message_handler(load_price_model, state=FSMShop.Price_model)
    dp.register_message_handler(load_photo_model, content_types=['photo'], state=FSMShop.Photo_model)
    dp.register_message_handler(load_submit, state=FSMShop.Submit_model)








