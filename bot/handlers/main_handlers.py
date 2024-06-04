from aiogram import types
from api.users.users import UserAPI
from bot.buttons.reply_buttons.main_buttons import m_buttons
from bot.models.users import User
from aiogram.fsm.context import FSMContext
from utils.json_db import read_json_file, write_json_file


async def start_handler(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    json_data = read_json_file('users.json')
    users_id = []

    for data in json_data:
        users_id.append(data['telegram_id'])

    if telegram_id not in users_id:
        await state.set_state(User.fullname)
        await message.answer('Assalomu aleykum! Iltimos ism familiyangizni kiriting.')

    else:
        await message.answer('Assalomu aleykum!', reply_markup=m_buttons())


async def fullname_handler(message: types.Message, state: FSMContext):
    json_data = read_json_file('users.json')

    if len(message.text.split()) == 2:
        data = {
            'first_name': message.text.split()[0],
            'last_name': message.text.split()[1],
            'username': message.from_user.username,
            'telegram_id': message.from_user.id
        }
        UserAPI().add_user(data)
        json_data.append({"telegram_id": data['telegram_id']})
        write_json_file('users.json', json_data)
        await state.update_data(fullname=message.text)
        await state.clear()
        await message.answer('Rahmat!', reply_markup=m_buttons())

    else:
        await state.set_state(User.fullname)
        await message.answer('Iltimos ism familiyangizni to\'g\'ri kiriting!')
