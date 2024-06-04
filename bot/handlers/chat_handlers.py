from aiogram import types
from api.chats.chats import ChatAPI


async def chats_handler(message: types.Message):
    text = ''
    number = 1

    for chat in ChatAPI().chat_list():
        text += f"{number}. [{chat['name']}]({chat['link']})\n"
        number += 1

    await message.answer(text, parse_mode='Markdown')
