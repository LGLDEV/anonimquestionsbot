from core import bot, dp
from aiogram import executor
from config import parser
from handlers import *
from utils import create_db


async def on_startup(dp):
    await bot.send_message(chat_id=parser('ADMIN_ID'),text="Bot ishladi")
    print("> Bot ishga tushirildi")



if __name__ =="__main__":
    create_db()
    executor.start_polling(dp, on_startup=on_startup)

