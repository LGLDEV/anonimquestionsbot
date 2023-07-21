from core import bot, dp
from aiogram import types
from utils import Query
from models import Admin
from markups import admin_markup, founder_markup


query = Query(Admin)


@dp.message_handler(commands=['admin', 'panel'])
async def display_menu(msg: types.Message):
	admin = query.get_admin(admin_id=msg.from_user.id)
	if not admin:
		return await msg.answer("<b>Admin emas ekansiz uzur</b>")
	else:
		if admin.admin_role == "founder":
			print("founder")
			return await msg.answer("<b>Assalomu Aleykum</b>", reply_markup=founder_markup)
		elif admin.admin_role == "admin":
			print("admin")
			return await msg.answer("<b>Assalomu Aleykum</b>", reply_markup=admin_markup)


