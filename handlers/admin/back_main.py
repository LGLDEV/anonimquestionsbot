from core import bot, dp
from aiogram import types
from utils import Query
from models import Admin
from markups import admin_markup, founder_markup


query = Query(Admin)


@dp.callback_query_handler(text="home")
async def display_menu(call: types.CallbackQuery):
	admin = query.get_admin(admin_id=call.from_user.id)
	if admin:
		await call.message.delete()
		if admin.admin_role == "founder":
			return await call.message.answer("<b>Assalomu Aleykum</b>", reply_markup=founder_markup)
		elif admin.admin_role == "admin":
			return await call.message.answer("<b>Assalomu Aleykum</b>", reply_markup=admin_markup)
	else:
		await call.message.delete()
		await call.message.answer("<b>Siz admin emas ekansiz</b>")