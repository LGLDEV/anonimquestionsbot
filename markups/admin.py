from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



founder_markup = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text="📊 Statistika", callback_data="stat"),
		InlineKeyboardButton(text="📤 Xabar yuborish", callback_data="send"),

	], 
	[
		InlineKeyboardButton(text="➕ Admin", callback_data="add_admin"),
		InlineKeyboardButton(text="➖ Admin", callback_data="remove_admin"),
	]
])





admin_markup = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text="📊 Statistika", callback_data="stat"),
	],
	[
		InlineKeyboardButton(text="📤 Xabar yuborish", callback_data="send"),
	]
])




   


    