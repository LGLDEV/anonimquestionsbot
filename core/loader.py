from config import parser
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=parser('TOKEN'), parse_mode='HTML')
dp = Dispatcher(bot=bot, storage=MemoryStorage())
