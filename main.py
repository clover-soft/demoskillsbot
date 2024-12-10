import asyncio
from config.config import Config
import logging
from logging.handlers import RotatingFileHandler
from database.initdb import InitDB
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

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


# async def before_handler(update: types.Update, call: types.CallbackQuery = None):
#     print('Before handler')
#     # Выполняем методы до обработки сообщения

# async def after_handler(update: types.Update, call: types.CallbackQuery = None):
#     print('After handler')
#     # Выполняем методы после обработки сообщения


class Form(StatesGroup):
    name = State()
    like_bots = State()
    language = State()


@dp.message(CommandStart())
async def start_command(message: Message):
    from handlers.start_command import HandlerStartCommand
    await HandlerStartCommand().handle_request(message)


# обработка сообщений
@dp.message()
async def echo_handler(message: Message) -> None:
    from handlers.echo import HandlerEcho
    await HandlerEcho().handle_request(message)


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
