from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from messages import messages
from data import data
from translator import maintranslator

startMarkup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='English', callback_data="0")],
    [InlineKeyboardButton(text='Русский', callback_data="1")],
    [InlineKeyboardButton(text='Espaniol', callback_data="2")]
])

async def mainMarkup(userlang:int):
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text=messages.MAINKB[userlang][0]))
    builder.add(KeyboardButton(text=messages.MAINKB[userlang][1]))   
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

async def langMarkup(userlang:int):
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text=messages.BACKKB[userlang]))
    for (key, value) in maintranslator.LANGUAGES_TRANSLATED.items():
        builder.add(KeyboardButton(text=value[userlang]))
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

async def changeMarkup(userlang: int):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=messages.CANGELANGSKB[userlang][0], callback_data="srcl"),
                InlineKeyboardButton(text=messages.CANGELANGSKB[userlang][1], callback_data="destl"),
            ],
            [
                InlineKeyboardButton(text=messages.CANGELANGSKB[userlang][2], callback_data="back"),
            ],
        ]
    )
    return markup