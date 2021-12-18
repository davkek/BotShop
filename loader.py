from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.db.storage import DatabaseManager

BOT_TOKEN = "2044910869:AAEjJhJ1bVHljxJf9S0h88JrsWm3bG_2uRA"
ADMINS = [705115861, 84143926]

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = DatabaseManager("data/database.db")
