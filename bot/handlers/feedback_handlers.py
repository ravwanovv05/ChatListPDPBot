from aiogram import Bot, types
from aiogram.fsm.context import FSMContext
from api.feedbacks.feedbacks import FeedbackAPI
from bot.models.feedbacks import Feedback


async def feedback_handler(message: types.Message, state: FSMContext):
    await state.set_state(Feedback.text)
    await message.answer('O\'z fikringizni qoldiring.')


async def get_feedback_handler(message: types.Message, state: FSMContext):
    data = {
        'text': message.text,
        'telegram_id': message.from_user.id,
        'telegram_user_id': None
    }
    FeedbackAPI().add_feedback(data)
    await state.update_data(text=message.text)
    await state.clear()
    await message.answer('Rahmat!')


