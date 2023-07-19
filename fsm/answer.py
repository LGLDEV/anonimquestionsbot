from aiogram.dispatcher.filters.state import State, StatesGroup



class Answer(StatesGroup):
	answer_id = State()

