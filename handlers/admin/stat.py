from core import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext





@dp.message_handler(commands=['test'])
async def sla(msg: types.Message):
    return await msg.answer("Hello World")



@dp.callback_query_handler(text="stat")
async def action_reply(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "Salom")

