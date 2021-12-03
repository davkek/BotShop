import logging
import aiogram
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '2108561672:AAFyOpFG5lMrjpEl1b3Fxi3EXPpfK3tQVRE'

# Конфигурация logging
logging.basicConfig(level=logging.INFO)

admin = 'Mikee'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# Клавиатура для начало
button_1 = KeyboardButton('Категории')
button_2 = KeyboardButton('Помощь')
button_3 = KeyboardButton('Отзыв')

start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_kb.row(button_1, button_2)
start_kb.row(button_3)

button_back = KeyboardButton('Назад')
back_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_back)

# Виды премиумов
spotify_kb = InlineKeyboardButton('Spotify Premium', callback_data='spotify_kb')
netflix_kb = InlineKeyboardButton('Netflix Premium', callback_data='netflix_kb')
youtube_kb = InlineKeyboardButton('YouTube Premium', callback_data='youtube_kb')
back = InlineKeyboardButton('Назад', callback_data='back')
inline_kb1 = InlineKeyboardMarkup().add(spotify_kb, netflix_kb, youtube_kb)
inline_kb1.add(back)

# Премиум Spotyfy
spoti_t1 = InlineKeyboardButton('Spotify Premium на 1 месяц', callback_data='spoti_t1')
spoti_t2 = InlineKeyboardButton('Spotify Premium на 6 месяц', callback_data='spoti_t2')
spoti_back = InlineKeyboardButton('Назад ', callback_data='spoti_back')
spotify_back = InlineKeyboardButton('Назад ко всем категориям', callback_data='spotify_back')
spotitime_kb = InlineKeyboardMarkup()
spotitime_kb.add(spoti_t1)
spotitime_kb.add(spoti_t2)
spotitime_kb.add(spoti_back)
spotitime_kb.add(spotify_back)
sp_ot = InlineKeyboardButton('Назад', callback_data='sp_ot')
sp_back = InlineKeyboardMarkup().add(sp_ot)

# Премиум Netflix
net_t1 = InlineKeyboardButton('Netflix Premium на 1 месяц', callback_data='net_t1')
net_t2 = InlineKeyboardButton('Netflix Premium на 6 месяц', callback_data='net_t2')
net_back = InlineKeyboardButton('Назад ', callback_data='net_back')
netflix_back = InlineKeyboardButton('Назад ко всем категориям', callback_data='netflix_back')
nt_ex = InlineKeyboardButton('Назад', callback_data='nt_ex')
nt_back = InlineKeyboardMarkup().add(nt_ex)
nettime_kb = InlineKeyboardMarkup()
nettime_kb.add(net_t1)
nettime_kb.add(net_t2)
nettime_kb.add(net_back)
nettime_kb.add(netflix_back)

# Премиум YouTube
yout_t1 = InlineKeyboardButton('Yotube Premium на 1 месяц', callback_data='yout_t1')
yout_t2 = InlineKeyboardButton('Yotube Premium на 6 месяц', callback_data='yout_t2')
yout_back = InlineKeyboardButton('Назад ', callback_data='yout_back')
youtube_back = InlineKeyboardButton('Назад ко всем категориям', callback_data='youtube_back')
yt_ex = InlineKeyboardButton('Назад', callback_data='yt_ex')
yt_back = InlineKeyboardMarkup().add(yt_ex)
youttime_kb = InlineKeyboardMarkup()
youttime_kb.add(yout_t1)
youttime_kb.add(yout_t2)
youttime_kb.add(yout_back)
youttime_kb.add(youtube_back)

@dp.message_handler(commands = ['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЯ бот Ropi.\nВы зашли в лучший магазин разных премиумов!!!\nКак понимаю вы хотите купить премиум.\n Зайдите в категории:", reply_markup = start_kb)

# Выбор категории
@dp.message_handler(text = 'Категории')
async def categories(message: types.Message):
    await bot.send_message(chat_id = message.chat.id, text = ' Что из этого вы хотите приобрести: ', reply_markup = inline_kb1)

@dp.message_handler(text = 'Помощь')
async def categories(message: types.Message):
    await bot.send_message(chat_id = message.chat.id, text = ' У вас произошла ошибка?\nНапишите: @ropiplay ', reply_markup = back_kb)

@dp.message_handler(text = 'Отзыв')
async def categories(message: types.Message):
    await bot.send_message(chat_id = message.chat.id, text = ' Отзывы скоро будут', reply_markup = back_kb)

@dp.message_handler(text = 'Назад')
async def categories(message: types.Message):
    await bot.send_message(chat_id = message.chat.id, text='Ты вернулся в главное меню.', reply_markup = start_kb)
# инлайн для SpotiFy
@dp.callback_query_handler()
async def handler_call(call: types.CallbackQuery):
    chat_id = call.from_user.id
    if call.data == 'spotify_kb':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, 'Какой Spotify вы хотите?' , reply_markup = spotitime_kb)
    elif call.data == 'spoti_t1':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, f'Вы хотите купить Spotify на 1 месяц?\nЕсли да, то напишите: {admin}.\nЕсли нет, нажмите назад:' , reply_markup = sp_back)
    elif call.data == 'spoti_t2':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, f'Вы хотите купить Spotify на 6 месяц?\nЕсли да, то напишите: {admin}.\nЕсли нет, нажмите назад:' , reply_markup = sp_back)
    elif call.data == 'sp_ot':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, 'Вы вернулись назад.' , reply_markup = spotitime_kb)
    elif call.data == 'spoti_back':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, 'Вы вернулись назад.' , reply_markup = inline_kb1)
    elif call.data == 'spotify_back':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, 'Вы вернулись на главное меню.' , reply_markup = start_kb)
    elif call.data == 'netflix_kb':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, 'Какой Netflix вы хотите?' , reply_markup = nettime_kb)
    elif call.data == 'net_t1':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, f'Вы хотите купить Netflix на 1 месяц?\nЕсли да, то напишите: {admin}.\nЕсли нет, нажмите назад:' , reply_markup = nt_back)
    elif call.data == 'net_t2':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, f'Вы хотите купить Netflix на 6 месяц?\nЕсли да, то напишите: {admin}.\nЕсли нет, нажмите назад:' , reply_markup = nt_back)
    elif call.data == 'nt_ex':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, 'Вы вернулись назад.' , reply_markup = nettime_kb)
    elif call.data == 'net_back':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, 'Вы вернулись назад.' , reply_markup = inline_kb1)
    elif call.data == 'netflix_back':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, 'Вы вернулись на главное меню.' , reply_markup = start_kb)
    elif call.data == 'youtube_kb':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, 'Какой Spotify вы хотите?' , reply_markup = youttime_kb)
    elif call.data == 'yout_t1':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, f'Вы хотите купить YouTube на 1 месяц?\nЕсли да, то напишите: {admin}.\nЕсли нет, нажмите назад:' , reply_markup = yt_back)
    elif call.data == 'yout_t2':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, f'Вы хотите купить YouTube на 6 месяц?\nЕсли да, то напишите: {admin}.\nЕсли нет, нажмите назад:' , reply_markup = yt_back)
    elif call.data == 'yt_ex':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, 'Вы вернулись назад.' , reply_markup = youttime_kb)
    elif call.data == 'yout_back':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, 'Вы вернулись назад.' , reply_markup = inline_kb1)
    elif call.data == 'youtube_back':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, 'Вы вернулись на главное меню.' , reply_markup = start_kb)
    elif call.data == 'back':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id, 'Вы вернулись на главное меню.' , reply_markup = start_kb)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)