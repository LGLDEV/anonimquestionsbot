from core import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from utils import Query
from models import User


query = Query(User)






@dp.callback_query_handler(text="stat")
async def action_reply(call: types.CallbackQuery):
    await call.message.delete()
    count = query.get_count()
    await bot.send_message(call.from_user.id, f"<b>📊 Botimiz statistikasi:\n\n Barcha userlar soni: <code>{count}</code>ta</b>")

