from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from repository.states_from import StatesForm
from aiogram.fsm.context import FSMContext


class HandlerMainMenu:
    markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='Настройки', callback_data='/settings'),
            KeyboardButton(text='GPT-3.5-Turbo',
                           callback_data='/gpt-35-turbo')
        ]
    ], resize_keyboard=True)

    def handle_request(self, message: Message):
        callback_data = message.text
        if callback_data == '/settings':
            from handlers.settings import Settings
        pass
