from aiogram import types
from aiogram.dispatcher.fsm.context import FSMContext


async def start(message: types.Message, state: FSMContext):
    await state.set_state(None)
    await message.answer('hello')
