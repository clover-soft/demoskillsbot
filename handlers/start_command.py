from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

class HandlerStartCommand:
    async def handle_request(self, message: Message):
        from services.user_service import UserService
        from utils.translate import Translate
        tg_user_id = message.from_user.id
        tg_user_name = message.from_user.full_name
        tg_user_json = message.from_user.model_dump_json()
        user = UserService().add_user(tg_user_id, tg_user_name, tg_user_json)
        response = Translate.get_phrase(user, 'hello', name=user.tg_user_name)
        keyboard = ReplyKeyboardMarkup(keyboard=[
            [
                KeyboardButton(text='Настройки', callback_data='settings'),
                KeyboardButton(text='GPT-3.5-Turbo',
                               callback_data='gpt-35-turbo')
            ]
        ], resize_keyboard=True)
        await message.answer(response, reply_markup=keyboard)
