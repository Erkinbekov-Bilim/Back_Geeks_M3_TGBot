# main_db.py

import sqlite3
from db import queries


db = sqlite3.connect('db/registered.sqlite3')
db_store = sqlite3.connect('db/store.sqlite3')

cursor = db.cursor()
cursor_store = db_store.cursor()


async def dataBase_create():
    if db:
        print("База данных подключена!")

    cursor.execute(queries.CREATE_TABLE_registered)
    cursor_store.execute(queries.CREATE_TABLE_store)
    cursor_store.execute(queries.CREATE_TABLE_product_details)

async def sql_insert_registered(fullname, age, gender, email, photo):
    cursor_store.execute(queries.INSERT_registered_QUERY, (
        fullname, age, gender, email, photo
    ))
    db.commit()

async def sql_insert_store(product_name, product_size, product_price, product_photo, product_id):
    cursor_store.execute(queries.INSERT_store_QUERY, (
        product_name, product_size, product_price, product_photo, product_id
    ))
    db_store.commit()

async def sql_insert_product_details(product_id, product_category, product_info):
    cursor_store.execute(queries.INSERT_product_details_QUERY, (
        product_id, product_category, product_info
    ))
    db_store.commit()


