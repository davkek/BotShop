import logging
from aiogram import Dispatcher, Bot, executor, types
import menu as nav

TOKEN = "2108561672:AAFyOpFG5lMrjpEl1b3Fxi3EXPpfK3tQVRE"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user),
                           reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message_main_menu(message: types.Message):
    if message.text == 'Контакты':
        await bot.send_message(message.from_user.id, 'Контакты', reply_markup=nav.contactsMenu)
    elif message.text == 'Информация':
        await bot.send_message(message.from_user.id, 'Информация')
    elif message.text == 'Каталог':
        await bot.send_message(message.from_user.id, '-Пусто-', reply_markup=nav.catalogMenu)
    elif message.text == 'Поиск':
        await bot.send_message(message.from_user.id, 'Поиск', reply_markup=nav.searchMenu)
    elif message.text == 'Поиск по наименованию':
        await bot.send_message(message.from_user.id, 'Поиск по наименованию')
    elif message.text == 'Поиск по цене':
        await bot.send_message(message.from_user.id, 'Поиск по цене')
    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.mainMenu)
    elif message.text == 'Мои заказы':
        await bot.send_message(message.from_user.id, 'Вас заскамили хи-хи', reply_markup=nav.ordersMenu)
    elif message.text == 'Корзина':
        await bot.send_message(message.from_user.id, 'Список товаров', reply_markup=nav.cartMenu)
    elif message.text == 'Самовывоз':
        await bot.send_message(message.from_user.id, 'Вы выбрали самовывоз', reply_markup=nav.PaymentMenu)
    elif message.text == 'Доставка':
        await bot.send_message(message.from_user.id, 'Вы выбрали доставку', reply_markup=nav.PaymentMenu)
    elif message.text == 'Оплатить':
        await bot.send_message(message.from_user.id, 'Успешно оплачено')
    else:
        await message.reply('Неизвестная команда')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
