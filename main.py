import asyncio
from config.config import Config
import logging
from logging.handlers import RotatingFileHandler
from repository.initdb import InitDB
from repository.states_from import StatesForm
from aiogram import Bot, Dispatcher, Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

# инициализация бота и диспетчера
states_form_router = Router()
InitDB.init_db()

log_level = Config().get_config_item('LOG_LEVEL', logging.DEBUG)
log_file = Config().get_config_item('LOG_FILENAME', 'log/bot.log')
handler = RotatingFileHandler(log_file, maxBytes=200*1024*1024, backupCount=10)
formatter = logging.Formatter(
    '[%(asctime)s][%(name)s][%(levelname)s]%(message)s')
handler.setFormatter(formatter)


@states_form_router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    from handlers.start_command import HandlerStartCommand
    await HandlerStartCommand().handle_request(message, state)


@states_form_router.message(StatesForm.main_menu)
async def settings(message: Message, state: FSMContext):
    from handlers.main_menu import HandlerMainMenu
    await HandlerMainMenu().handle_request(message, state)


@states_form_router.message(StatesForm.settings)
async def settings(message: Message, state: FSMContext):
    from handlers.settings import HandlerSettings
    await HandlerSettings().handle_request(message, state)


@states_form_router.message(StatesForm.select_language)
async def settings(message: Message, state: FSMContext):
    from handlers.select_language import HandlerSelectLanguage
    await HandlerSelectLanguage().handle_request(message, state)

async def main() -> None:
    bot = Bot(token=Config().get_config_item('BOT_TOKEN'), default=DefaultBotProperties(
        parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(states_form_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
