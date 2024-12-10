from aiogram.fsm.state import StatesGroup, State

class StatesForm(StatesGroup):
    main_menu = State()
    settings = State()
    gpt35turbo = State()
    select_language = State()