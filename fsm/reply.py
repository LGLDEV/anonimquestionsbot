from aiogram.dispatcher.filters.state import State, StatesGroup

class Reply(StatesGroup):
    reply_id = State()
    message = State()
