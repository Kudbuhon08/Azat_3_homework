import sqlite3 
from aiogram import Bot,Dispatcher,executor,types
import logging
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext,filters
from aiogram.dispatcher.filters.state import State,StatesGroup

bot= Bot(token="7173354100:AAF1iwFZmVjPX33Ig9uBVZx8l55ETCb_Tw8")
dp= Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
 
m1wex=sqlite3.connect("BANK.db")
cursor=m1wex.cursor()
cursor.execute ("""CREATE TABLE IF NOT EXISTS user 
                (user_id INTEGER PRIMARY KEY,
                username VARCAR (100),
                balance  REAL DEFAULT (0),
                number_balance)""")
m1wex.commit()

strage=MemoryStorage()
dp.storage=strage
knopka=[
types.KeyboardButton("Баланс"),
types.KeyboardButton("Перевод"),
types.KeyboardButton("Пополнение")
]
start_knopka=types.ReplyKeyboardMarkup(resize_keyboard=True).add(*knopka)

@dp.message_handler(commands="start")
async def start (message:types.Message):
    user_id=message.from_user.id
    cursor.execute("SELECT * FROM user WHERE user_id=?,",(user_id))
    extech_user = cursor.fetchone()
    if not extech_user:
        cursor.execute(f"INSERT INTO user (user_id,username,number_balance) VALUES (?,?,?)",(user_id,message.from_user.username,message.from_user.id))
        m1wex.commit()

    user_info= f"Ваш ID: [{message.from_user.id}]"
    username+=f"Никнейм: [{message.from_user.username}]"

    await message.answer (f"Информация о вас:\n {user_info}",reply_markup=start_knopka)
    await message.answer("Привет! Этот бот Оптима банк \n/balance - посмотреть баланс \n/deposit - пополнить баланс \n/transfer - перевести на другой счет", reply_markup=start_knopka)

executor.start_polling(dp)