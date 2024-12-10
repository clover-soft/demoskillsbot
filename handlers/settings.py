from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from repository.states_from import StatesForm
from aiogram.fsm.context import FSMContext
from utils.translate import Translate

class HandlerSettings:
    markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='Язык', callback_data='/select_language'),
            KeyboardButton(text='Назад', callback_data='/main_menu')
        ]
    ], resize_keyboard=True)

    async def handle_request(self, message: Message, state: FSMContext):
        if message.text == '/main_menu':
            state.set_state(StatesForm.main_menu)
            from handlers.main_menu import HandlerMainMenu
            await message.edit_reply_markup(reply_markup=HandlerMainMenu().markup)            
        elif message.text == '/select_language':
            state.set_state(StatesForm.select_language)
            from handlers.select_language import HandlerSelectLanguage
            await message.edit_reply_markup(reply_markup=HandlerSelectLanguage().markup)
        else:
            await message.answer()
