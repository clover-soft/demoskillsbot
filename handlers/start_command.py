from aiogram.types import Message
from repository.states_from import StatesForm
from aiogram.fsm.context import FSMContext
from repository.states_from import StatesForm


class HandlerStartCommand:
    async def handle_request(self, message: Message, state: FSMContext):
        from services.user_service import UserService
        from utils.translate import Translate
        tg_user_id = message.from_user.id
        tg_user_name = message.from_user.full_name
        tg_user_json = message.from_user.model_dump_json()
        user = UserService().add_user(tg_user_id, tg_user_name, tg_user_json)
        if str(user.tg_user_json_dict['language_code']).lower() == 'ru':
            await state.update_data(select_language='ru')
        else:
            await state.update_data(select_language='en')
        response = Translate.get_phrase('hello', name=user.tg_user_name)
        state.set_state(StatesForm.main_menu)
        from handlers.main_menu import HandlerMainMenu
        await message.answer(response, reply_markup=HandlerMainMenu().markup)
