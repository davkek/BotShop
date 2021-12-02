from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu = InlineKeyboardButton('Главное меню', callback_data='menu')

"""----Главное меню---"""
markup = InlineKeyboardMarkup(row_width=2)
contact = InlineKeyboardButton('Контакты', callback_data='contact')
catalog = InlineKeyboardButton('Каталог', callback_data='catalog')
orders = InlineKeyboardButton('Мои заказы', callback_data='orders')
cart = InlineKeyboardButton('Корзина', callback_data='cart')
markup.add(contact, catalog, orders, cart)

"""----Каталог---"""
catalogMenu = InlineKeyboardMarkup(row_width=2)
search = InlineKeyboardButton('Поиск', callback_data='search')
catalogMenu.add(search, menu)

"""----Поиск---"""
searchMenu = InlineKeyboardMarkup(row_width=2)
valueSearch = InlineKeyboardButton('Поиск по наименованию', callback_data='valueSearch')
costSearch = InlineKeyboardButton('Поиск по цене', callback_data='costSearch')
searchMenu.add(valueSearch, costSearch, menu)

"""----Контакты---"""
contactMenu = InlineKeyboardMarkup(row_width=2)
contactMenu.add(menu)

"""----Мои заказы---"""
orderMenu = InlineKeyboardMarkup(row_width=2)
orderMenu.add(menu)

"""----Корзина---"""
cartMenu = InlineKeyboardMarkup(row_width=2)
pickup = InlineKeyboardButton('Самовывоз', callback_data='pickup')
delivery = InlineKeyboardButton('доставка', callback_data='delivery')
cartMenu.add(pickup, delivery, menu)

"""----Оплата---"""
paymentMenu = InlineKeyboardMarkup(row_width=2)
payment = InlineKeyboardButton('Оплатить', callback_data='payment')
paymentMenu.add(payment, menu)
