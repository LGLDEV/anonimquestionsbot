from core import bot, dp
from aiogram import types
from utils import Query
from models import User


query = Query(User)


@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message):
    query.create_user(user_id=msg.from_user.id)
    print(query.get_user(user_id=msg.from_user.id))
    await msg.answer("<b>Assalomu Aleykum</b>")
