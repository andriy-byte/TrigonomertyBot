from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


sin_text = "sin(x)"
cos_text = "cos(x)"
tg_text = "tg(x)"
ctg_text = "ctg(x)"

sin_text_callback = "sin"
cos_text_callback = "cos"
tg_text_callback = "tg"
ctg_text_callback = "ctg"

markup = InlineKeyboardMarkup(row_width=4)

sinus_button = InlineKeyboardButton(text=sin_text,callback_data=sin_text_callback)
cosinus_button = InlineKeyboardButton(text=cos_text,callback_data=cos_text_callback)
tangens_button = InlineKeyboardButton(text=tg_text,callback_data=tg_text_callback)
cotangens_button = InlineKeyboardButton(text=ctg_text,callback_data=ctg_text_callback)

markup.add(sinus_button, cosinus_button, tangens_button, cotangens_button)
