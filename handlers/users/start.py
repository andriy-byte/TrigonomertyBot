from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привіт, {message.from_user.full_name}!\nЯ бот який виконує чотири базові тригонометричні '
                         f'функції : сінус, косинус, тангенс, котангенс.\nВведіть будьяке число.\n'
                         f'ПОПЕРЕДЖЕННЯ : ВАШЕ ЧИСЛО БОТ СПРИЙМАТЕМЕ В РАДІАНАХ ')
