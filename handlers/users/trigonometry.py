from aiogram import types
from keyboards.inline import trigonometry
from aiogram.types import Message, CallbackQuery
from loader import dp
from math import sin, cos, tan, pi


@dp.message_handler(regexp='^[+-]?([0-9]+([.,][0-9]*)?|[.][0-9]+)$')
async def trigonometry_start(msg: Message):
    await msg.answer(text=str(float(str(msg.text).replace(",","."))), reply_markup=trigonometry.markup)


@dp.message_handler(content_types=types.ContentType.ANY)
async def inappropriate_msg(m: Message):
    await m.answer(text="Введіть число або введіть число коректно!!!")


@dp.callback_query_handler(text=trigonometry.sin_text_callback)
async def sin_x(c: CallbackQuery):
    num = float(str(c.message.text).replace(",","."))
    await c.message.answer(text=f"sin({str(num)}) = {str(sin(num))}")


@dp.callback_query_handler(text=trigonometry.cos_text_callback)
async def cos_x(c: CallbackQuery):
    num = float(str(c.message.text).replace(",","."))
    await c.message.answer(text=f"cos({str(num)}) = {str(cos(num))}")


@dp.callback_query_handler(text=trigonometry.tg_text_callback)
async def tg_x(c: CallbackQuery):
    num = float(str(c.message.text).replace(",","."))
    if num == pi / 2.0 or num == 3.0 * pi / 2.0:
        await c.message.answer(text=f"tg({str(num)}) = НЕІСНУЄ")
    else:
        await c.message.answer(text=f"tg({str(num)}) = {str(tan(num))}")


@dp.callback_query_handler(text=trigonometry.ctg_text_callback)
async def ctg_x(c: CallbackQuery):
    num = float(str(c.message.text).replace(",","."))
    if num == 0.0 or num == pi:
        await c.message.answer(text=f"сtg({str(num)}) = НЕІСНУЄ")
    else:
        def ctg(x):
            return cos(x)/sin(x)
        await c.message.answer(text=f"сtg({str(num)}) = {str(ctg(num))}")
