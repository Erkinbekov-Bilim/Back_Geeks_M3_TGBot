# fsm_shop.py

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import cancel_markup, start_markup, submit
from db import main_db
from buttons import cancel_markup


class FSMShop(StatesGroup):
    product_name = State()
    product_size = State()
    product_category = State()
    product_price = State()
    product_id = State()
    product_info = State()
    product_photo = State()
    product_collection = State()
    product_submit = State()


async def start_fsm_shop(message: types.Message):
    await message.answer('Введите название товара:', reply_markup=cancel_markup)
    await FSMShop.product_name.set()


async def load_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["product_name"] = message.text

    await FSMShop.next()
    await message.answer('Введите размер товара:')


async def load_product_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["product_size"] = message.text

    await FSMShop.next()
    await message.answer('Введите категорию товара:')


async def load_product_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["product_category"] = message.text

    await FSMShop.next()
    await message.answer('Введите цену товара:')

async def load_product_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["product_price"] = message.text

    await FSMShop.next()
    await message.answer('Отправьте артикул товара:')

async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["product_id"] = message.text

    await FSMShop.next()
    await message.answer('Отправьте информацию о товаре:')

async def load_product_info(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["product_info"] = message.text

    await FSMShop.next()
    await message.answer('Отправьте фото товара:')

async def load_product_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["product_photo"] = message.photo[-1].file_id

    await FSMShop.next()
    await message.answer('Отправьте коллекцию товара:')

async def load_product_collection(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["product_collection"] = message.text

    await FSMShop.next()
    await message.answer(f'Верны ли данные?', reply_markup=submit)
    await message.answer_photo(photo=data["product_photo"],
                               caption=f'Название товара - {data["product_name"]}\n'
                               f'Размер товара - {data["product_size"]}\n'
                               f'Категория товара - {data["product_category"]}\n'
                               f'Цена товара - {data["product_price"]}\n'
                               f'Артикул товара - {data["product_id"]}\n'
                               f'Информация о товаре - {data["product_info"]}\n'
                               f'Коллекция товара - {data["product_collection"]}'
                               )


async def load_submit(message: types.Message, state: FSMContext):
    if message.text == "Да":
        async with state.proxy() as data:
            # Запись в базу
            await main_db.sql_insert_store(
                product_name=data["product_name"],
                product_size=data["product_size"],
                product_price=data["product_price"],
                product_id=data["product_id"],
                product_photo=data["product_photo"]
            )

            await main_db.sql_insert_product_details(
                product_category=data["product_category"],
                product_info=data["product_info"],
                product_id=data["product_id"]
            )

            await main_db.sql_insert_collection_products(
                product_id=data["product_id"],
                product_collection=data["product_collection"]
            )

            await message.answer("Ваши данные в базе!", reply_markup=start_markup)
            await state.finish()

    elif message.text == "Нет":
        await message.answer("Хорошо, отменено!", reply_markup=start_markup)
        await state.finish()
    else:
        await message.answer("Введите 'Да' или 'Нет'")


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()
        await message.answer("Отменено!", reply_markup=start_markup)


def register_handlers_fsm_shop(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals="cancel", ignore_case=True), state="*")

    dp.register_message_handler(start_fsm_shop, commands=['shop'], state=None)
    dp.register_message_handler(load_product_name, state=FSMShop.product_name)
    dp.register_message_handler(load_product_size, state=FSMShop.product_size)
    dp.register_message_handler(load_product_category, state=FSMShop.product_category)
    dp.register_message_handler(load_product_price, state=FSMShop.product_price)
    dp.register_message_handler(load_product_id, state=FSMShop.product_id)
    dp.register_message_handler(load_product_info, state=FSMShop.product_info)
    dp.register_message_handler(load_product_photo, content_types=['photo'], state=FSMShop.product_photo)
    dp.register_message_handler(load_product_collection, state=FSMShop.product_collection)
    dp.register_message_handler(load_submit, state=FSMShop.product_submit)








