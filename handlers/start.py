from core import bot, dp
from aiogram import types 
from aiogram.dispatcher import FSMContext
from utils import Query
from models import User
from config import parser
from fsm import Reply
from markups import back_markup, rep_markup


query = Query(User)


@dp.message_handler(commands=['start'], state="*")
async def cmd_start(msg: types.Message, state: FSMContext):
    try:
        user = query.get_user(msg.from_user.id)
        if msg.get_args():
            idx = query.get_user(msg.get_args())
            if not idx:
                await msg.answer("<b>⚠️ Bu foydalanuvchi mavjud emas</b>")
                await msg.answer(f"<b>Bu sizning shaxsiy havolangiz:\n\nhttps://t.me/{parser('BOT_NAME')}?start={msg.from_user.id}\n\nUlashish orqali anonim suhbat quring!</b>")
                return await state.finish()
            if not user:
                query.create_user(msg.from_user.id)
                await msg.answer("<b>Xabaringizni yuboring: </b>", reply_markup=back_markup)
                await state.update_data({"message_args": msg.get_args()})
                return await state.set_state(Reply.reply_id.state)
            else:
                await msg.answer("<b>Xabaringizni yuboring: </b>", reply_markup=back_markup)
                await state.update_data({"reply_id": msg.get_args()})
                return await state.set_state(Reply.reply_id.state)
        else:
            if not user:
                query.create_user(msg.from_user.id)
                return await msg.answer(f"<b>Bu sizning shaxsiy havolangiz:\n\nhttps://t.me/{parser('BOT_NAME')}?start={msg.from_user.id}\n\nUlashish orqali anonim suhbat quring!</b>")
            return await msg.answer(f"<b>Bu sizning shaxsiy havolangiz:\n\nhttps://t.me/{parser('BOT_NAME')}?start={msg.from_user.id}\n\nUlashish orqali anonim suhbat quring!</b>")
    except:
        return await msg.answer("<b>🚫 Xatolik yuz berdi</b>")
        





@dp.message_handler(state=Reply.reply_id)
async def reply_id(msg: types.Message, state: FSMContext):
    try:
        if msg.text == "❌ Bekor qilish":
            await msg.answer(f"<b>Bu sizning shaxsiy havolangiz:\n\nhttps://t.me/{parser('BOT_NAME')}?start={msg.from_user.id}\n\nUlashish orqali anonim suhbat quring!</b>", reply_markup=types.ReplyKeyboardRemove())
            return await state.finish()
        text = msg.text 
        data = await state.get_data()
        await bot.send_message(data['reply_id'], text=text, reply_markup=rep_markup(data['reply_id']))
        await state.finish()
        return await msg.answer(f"<b>Bu sizning shaxsiy havolangiz:\n\nhttps://t.me/{parser('BOT_NAME')}?start={msg.from_user.id}\n\nUlashish orqali anonim suhbat quring!</b>")
    except Exception as exe:
        print(exe)
        return await msg.answer("<b>🚫 Xatolik yuz berdi</b>")
