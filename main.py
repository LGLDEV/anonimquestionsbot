from core import bot, dp
from aiogram import executor
from config import parser
from handlers import start



async def on_startup(dp):
    await bot.send_message(chat_id=parser('ADMIN_ID'),text="Bot ishladi")
    print("> Bot ishga tushirildi")



if __name__ =="__main__":
    executor.start_polling(dp, on_startup=on_startup)

