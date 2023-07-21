from core import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from utils import Query
from models import Admin, User
from markups import admin_markup, founder_markup, back_main
from fsm import Mailing

query = Query(Admin)
user_query = Query(User)


@dp.callback_query_handler(text="send")
async def display_menu(call: types.CallbackQuery, state: FSMContext):
	admin = query.get_admin(admin_id=call.from_user.id)
	if not admin:
		return await call.message.answer("<b>Admin emas ekansiz uzur</b>")
	else:
		await call.message.delete()
		await call.message.answer("<b>Xabaringizni yuboring</b>")
		return await state.set_state(Mailing.message.state)


@dp.message_handler(content_types=['text', 'photo'],state=Mailing.message)
async def mailing(msg: types.Message, state: FSMContext):
	admin = query.get_admin(admin_id=msg.from_user.id)
	if not admin:
		return await msg.answer("<b>Admin emas ekansiz uzur</b>")
	else:
		text = msg.text

		try:
			users = user_query.get_users()
			err = 0
			active = 0
			for user in users:
				try:
					active += 1
					await msg.copy_to(chat_id=user.user_id)
				except Exception as e:
					err += 1
			await msg.answer(f"<b>📤 Xabar yuborildi\n\n<code>✅ {active}ta</code> - Xabar yetib bordi\n<code>❌ {err}ta</code> - Xabar yetib bormadi</b>", reply_markup=back_main)
			await state.finish()
				
		except Exception as e:
			return await msg.answer("<b>🚫 Xatolik yuz berdi</b>", reply_markup=back_main)
		