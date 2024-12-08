import asyncio
from config.config import Config
import logging
from logging.handlers import RotatingFileHandler
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from database.initdb import InitDB
from services.user_service import UserService
# инициализация бота и диспетчера
bot = Bot(token=Config().get_config_item('BOT_TOKEN'), default=DefaultBotProperties(
    parse_mode=ParseMode.HTML))
dp = Dispatcher()
InitDB.init_db()

log_level = Config().get_config_item('LOG_LEVEL', logging.DEBUG)
log_file = Config().get_config_item('LOG_FILENAME', 'log/bot.log')
handler = RotatingFileHandler(log_file, maxBytes=200*1024*1024, backupCount=10)
formatter = logging.Formatter(
    '[%(asctime)s][%(name)s][%(levelname)s]%(message)s')
handler.setFormatter(formatter)


# обработка команды /start

@dp.message(CommandStart())
async def start_command(message: Message):
    full_name = message.from_user.full_name.encode('utf-8')
    UserService().add_user(message.from_user.id, full_name, message.from_user.username)
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!")


# обработка сообщений
@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        user_name = 'Unknown'
        User = UserService().get_user(message.from_user.id)
        if User:
            user_name = User.full_name
        await message.answer(f"Hi, {user_name}!")
        # await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
