from core import bot, dp
from aiogram import types
from utils import Query
from models import Admin
from markups import types_markup, back_main, all_admins
from aiogram.dispatcher import FSMContext
from fsm import Add

query = Query(Admin)


@dp.callback_query_handler(text="add_admin")
async def display_menu(call: types.CallbackQuery, state: FSMContext):
	admin = query.get_admin(admin_id=call.from_user.id)
	if admin:
		await call.message.delete()
		await call.message.answer("🆔 Id kiriting")
		await state.set_state(Add.admin_id.state)
	else:
		await call.message.delete()
		await call.message.answer("<b>Siz admin emas ekansiz</b>")


@dp.message_handler(state=Add.admin_id)
async def add_admin(msg: types.Message, state: FSMContext):
	admin_id = msg.text 
	if admin_id.isdigit():
		await msg.answer("💬 Admin turini tanlang", reply_markup=types_markup)
		await state.update_data({"admin_id": admin_id})
		return await state.set_state(Add.admin_type.state)
	else:
		await msg.answer("ID xato kiritildi", reply_markup=back_main)
		return await state.finish()


@dp.callback_query_handler(text="type_founder", state=Add.admin_type)
async def set_type(call: types.CallbackQuery, state: FSMContext):
	await call.message.delete()
	admin_type = call.data[5:]
	data = await state.get_data()
	query.create_admin(admin_id=data["admin_id"], admin_role="founder")
	await state.finish()
	return await call.message.answer("Admin muafaqiyatli qo'shildi", reply_markup=back_main)


@dp.callback_query_handler(text="type_admin", state=Add.admin_type)
async def set_type(call: types.CallbackQuery, state: FSMContext):
	await call.message.delete()
	admin_type = call.data[5:]
	data = await state.get_data()
	query.create_admin(admin_id=data["admin_id"], admin_role="admin")
	await state.finish()
	return await call.message.answer("Admin muafaqiyatli qo'shildi", reply_markup=back_main)


# delete admin functions
@dp.callback_query_handler(text="remove_admin")
async def display_menu(call: types.CallbackQuery):
	admin = query.get_admin(admin_id=call.from_user.id)
	admins = query.get_users()
	if admin:
		await call.message.delete()
		await call.message.answer("💬 Qaysi adminni o'chirish kerak", reply_markup=all_admins(admins=admins))
	else:
		await call.message.delete()
		await call.message.answer("<b>Siz admin emas ekansiz</b>")


@dp.callback_query_handler(text_contains="del_")
async def del_admin(call: types.CallbackQuery):
	await call.message.delete()
	admin_id = call.data[4:]
	query.delete_admin(admin_id=admin_id)
	await call.message.answer("<b>🗑 Admin o'chirib tashlandi</b>", reply_markup=back_main)

