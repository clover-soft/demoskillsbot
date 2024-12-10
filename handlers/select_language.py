from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from repository.states_from import StatesForm
from aiogram.fsm.context import FSMContext


class HandlerSelectLanguage:
    markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='English', callback_data='/lang_en'),
            KeyboardButton(text='Русский', callback_data='/lang_ru')
        ]
    ], resize_keyboard=True)

    def handle_request(self, message: Message, state: FSMContext):
        state.clear()
        pass
