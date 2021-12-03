import logging
from aiogram import Dispatcher, Bot, executor, types
import markup as m

TOKEN = "2108561672:AAFyOpFG5lMrjpEl1b3Fxi3EXPpfK3tQVRE"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user), reply_markup=m.mainMenu)


@dp.callback_query_handler(lambda c: c.data == 'menu')
async def command(call: types.callback_query):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, 'Главное меню', reply_markup=m.mainMenu)


@dp.message_handler(text = 'Контакты')
async def command(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.send_message(chat_id=message.chat.id, text=' информатион: ',
                           reply_markup=m.contactMenu)


@dp.message_handler(text = 'Каталог')
async def command(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.send_message(chat_id=message.chat.id, text='каталог', reply_markup=m.catalogMenu)


@dp.callback_query_handler(lambda c: c.data == 'search')
async def command(call: types.callback_query):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, 'Поиск', reply_markup=m.searchMenu)


@dp.message_handler(text = 'Мои заказы')
async def command(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.send_message(chat_id=message.chat.id, text='Вас заскамили хи-хи', reply_markup=m.orderMenu)


@dp.message_handler(text = 'Корзина')
async def command(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.send_message(chat_id=message.chat.id, text='заказек', reply_markup=m.cartMenu)


@dp.callback_query_handler(lambda c: c.data == 'pickup')
async def command(call: types.callback_query):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, 'Оплата', reply_markup=m.paymentMenu)


@dp.callback_query_handler(lambda c: c.data == 'delivery')
async def command(call: types.callback_query):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, 'Оплата', reply_markup=m.paymentMenu)


@dp.callback_query_handler(lambda c: c.data == 'payment')
async def command(call: types.callback_query):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, 'Успешно оплачено', reply_markup=m.mainMenu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
