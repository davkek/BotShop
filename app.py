from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup
from loader import *
import filters
import logging

filters.setup(dp)

menu_message = "Меню"


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row(menu_message)

    await message.answer(
        """Привет! 👋
    
🛍️ Чтобы перейти в каталог и выбрать приглянувшиеся товары воспользуйтесь кнопкой.

    """,
        reply_markup=markup,
    )


async def on_startup():
    logging.basicConfig(level=logging.DEBUG)
    db.create_tables()


async def on_shutdown():
    logging.warning("Shutting down..")
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bot down")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
