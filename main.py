import asyncio
import logging
import os
import sys
from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from dotenv import load_dotenv
from bot.handlers.chat_handlers import chats_handler
from bot.handlers.feedback_handlers import feedback_handler, get_feedback_handler
from bot.handlers.main_handlers import start_handler, fullname_handler
from bot.models.feedbacks import Feedback
from bot.models.users import User

load_dotenv()

token = os.getenv('BOT_TOKEN')


async def start():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    bot = Bot(token=token)

    dp = Dispatcher()
    dp.message.register(start_handler, Command(commands='start'))
    dp.message.register(fullname_handler, User.fullname)
    dp.message.register(feedback_handler, lambda message: message.text == 'Taklif/Shikoyat')
    dp.message.register(get_feedback_handler, Feedback.text)
    dp.message.register(chats_handler, lambda message: message.text == 'PDP Academy groups and bots')

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
