from aiogram.types import Message


class HandlerEcho:
    async def handle_request(self, message: Message):
        await message.send_copy(chat_id=message.from_user.id)
