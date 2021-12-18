from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup

from app import menu_message
from loader import dp
from filters import IsAdmin, IsUser

catalog = "🛍️ Каталог"
balance = "💰 Баланс"
cart = "🛒 Корзина"
delivery_status = "🚚 Статус заказа"
info = "📄 Наш адрес"

settings = "⚙️ Настройка каталога"
sub_settings = "⚙️ Настройка подкаталога"
orders = "🚚 Заказы"
questions = "❓ Вопросы"
db_work = "🗃️ Работа с БД"


@dp.message_handler(IsAdmin(), commands=["admin"])
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(settings, sub_settings)
    markup.add(questions, orders, db_work)

    await message.answer("Меню", reply_markup=markup)


@dp.message_handler(text=menu_message)
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True, resize_keyboard=True)
    markup.add(catalog, cart, info)
    # markup.add(cart)
    # markup.add(delivery_status)

    await message.answer("Меню", reply_markup=markup)
