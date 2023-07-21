from aiogram.dispatcher.filters.state import State, StatesGroup



class Add(StatesGroup):
	admin_id = State()
	admin_type = State()

