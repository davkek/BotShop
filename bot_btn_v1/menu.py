from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

""" ---Main menu--- """
btnContacts = KeyboardButton('Контакты')
btnCatalog = KeyboardButton('Каталог')
btnMyOrders = KeyboardButton('Мои заказы')
btnCart = KeyboardButton('Корзина')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnContacts, btnCatalog, btnMyOrders, btnCart)

""" ---Contacts--- """
btnInfo = KeyboardButton('Информация')
contactsMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMain)

""" ---Catalog--- """
btnSearch = KeyboardButton('Поиск')
catalogMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSearch, btnMain)

""" ---Search--- """
btnValueSearch = KeyboardButton('Поиск по наименованию')
btnCostSearch = KeyboardButton('Поиск по цене')
searchMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnValueSearch, btnCostSearch, btnMain)

""" ---My orders>--- """
#btnInfo = KeyboardButton('Информация')
ordersMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)

""" ---Cart--- """
btnSelfPickup = KeyboardButton('Самовывоз')
btnDelivery = KeyboardButton('Доставка')
cartMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSelfPickup, btnDelivery, btnMain)

""" ---Payment--- """
btnPay = KeyboardButton('Оплатить')
PaymentMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPay, btnMain)

