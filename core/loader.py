from config import parser
from aiogram import Dispatcher, Bot


bot = Bot(token=parser('TOKEN'), parse_mode='HTML')
dp = Dispatcher(bot=bot)
