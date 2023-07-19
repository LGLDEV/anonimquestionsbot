from core import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from fsm import Answer
from markups import back_markup, rep_markup
from config import parser


@dp.callback_query_handler(state="*")
async def action_reply(call: types.CallbackQuery,state: FSMContext ):
	try:
		if "repl_" in call.data:
			data = call.data[5:]
			await state.update_data({"answer_id": data})
			await bot.send_message(call.from_user.id, "📤 Javobingizni yozing", reply_markup=back_markup)
			return await state.set_state(Answer.answer_id.state)
	except:
		return await msg.answer("<b>🚫 Xatolik yuz berdi</b>")



@dp.message_handler(state=Answer.answer_id)
async def reply_id(msg: types.Message, state: FSMContext):
    try:
        if msg.text == "❌ Bekor qilish":
            await msg.answer(f"<b>Bu sizning shaxsiy havolangiz:\n\nhttps://t.me/{parser('BOT_NAME')}?start={msg.from_user.id}\n\nUlashish orqali anonim suhbat quring!</b>", reply_markup=types.ReplyKeyboardRemove())
            return await state.finish()
        text = msg.text 
        data = await state.get_data()
        await bot.send_message(data["answer_id"], text=text, reply_markup=rep_markup(data['answer_id']))
        await state.finish()
        return await msg.answer(f"<b>Bu sizning shaxsiy havolangiz:\n\nhttps://t.me/{parser('BOT_NAME')}?start={msg.from_user.id}\n\nUlashish orqali anonim suhbat quring!</b>")
    except Exception as exe:
    	return await msg.answer("<b>🚫 Xatolik yuz berdi</b>")
