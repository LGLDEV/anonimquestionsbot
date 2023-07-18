from core import bot, dp
from aiogram import types



@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message):
    await msg.answer("<b>Assalomu Aleykum</b>")
