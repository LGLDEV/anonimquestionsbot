from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton






def rep_markup(idx):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="🔁 Javob yozish", callback_data=f"repl_{idx}")
    markup.add(button)
    return markup