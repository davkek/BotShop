from handlers.user.menu import db_work
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from loader import dp, bot
from filters import IsAdmin
from utils.db import csv_output_categories, csv_output_products, csv_input_categories, csv_input_products


@dp.message_handler(IsAdmin(), text=db_work)
async def process_database(message: Message):
    markup = InlineKeyboardMarkup(selective=True, row_width=1)
    markup.add(InlineKeyboardButton("Вывести данные", callback_data="output"),
               InlineKeyboardButton("Импортировать данные", callback_data="input"))
    await message.answer("Выберите действие: ", reply_markup=markup)


@dp.callback_query_handler(IsAdmin(), lambda c: c.data == 'output')
async def process_output(query: CallbackQuery):
    markup = InlineKeyboardMarkup(selective=True, row_width=1)
    markup.add(InlineKeyboardButton("Данные из таблицы categories", callback_data="cat_o"),
               InlineKeyboardButton("Данные из таблицы products", callback_data="prd_o"))
    await query.message.answer("Выберите таблицу: ", reply_markup=markup)


@dp.callback_query_handler(IsAdmin(), lambda c: c.data == 'cat_o')
async def cat_output(query: CallbackQuery):
    await bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
    csv_output_categories()
    await query.message.answer("Данные успешно записаны в файл")


@dp.callback_query_handler(IsAdmin(), lambda c: c.data == 'prd_o')
async def product_output(query: CallbackQuery):
    await bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
    csv_output_products()
    await query.message.answer("Данные успешно записаны в файл")


@dp.callback_query_handler(IsAdmin(), lambda c: c.data == 'input')
async def process_output(query: CallbackQuery):
    markup = InlineKeyboardMarkup(selective=True, row_width=1)
    markup.add(InlineKeyboardButton("Данные из таблицы categories", callback_data="cat_in"),
               InlineKeyboardButton("Данные из таблицы products", callback_data="prd_in"))
    await query.message.answer("Выберите таблицу: ", reply_markup=markup)


@dp.callback_query_handler(IsAdmin(), lambda c: c.data == 'cat_in')
async def cat_input(query: CallbackQuery):
    await bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
    csv_input_categories()
    await query.message.answer("Данные успешно записаны в базу данных")


@dp.callback_query_handler(IsAdmin(), lambda c: c.data == 'prd_in')
async def cat_input(query: CallbackQuery):
    await bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
    csv_input_products()
    await query.message.answer("Данные успешно записаны в базу данных")
