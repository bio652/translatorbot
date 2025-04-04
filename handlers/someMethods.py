from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from data import data
from kbs import keyboards
from states import states
from messages import messages
from translator import maintranslator

async def mainmenu(message: types.message, state: FSMContext):
    await state.clear()
    mainm = int(data.getUserlang(message.from_user.id))
    trlangs = data.getTranslangs(message.from_user.id)
    await message.answer(messages.MAINMESSAGE[mainm].format(trlang = maintranslator.LANGUAGES_TRANSLATED[trlangs[0]][mainm],tolang = maintranslator.LANGUAGES_TRANSLATED[trlangs[1]][mainm]), reply_markup = await keyboards.mainMarkup(mainm))

async def mainmenucb(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    mainm = int(data.getUserlang(callback.from_user.id))
    trlangs = data.getTranslangs(callback.from_user.id)
    await callback.message.answer(messages.MAINMESSAGE[mainm].format(trlang = maintranslator.LANGUAGES_TRANSLATED[trlangs[0]][mainm],tolang = maintranslator.LANGUAGES_TRANSLATED[trlangs[1]][mainm]), reply_markup = await keyboards.mainMarkup(mainm))
    
async def changemenulang(message: types.message, state: FSMContext):
    await state.set_state(states.Start.langselect)
    temp = await message.answer(".", reply_markup = keyboards.ReplyKeyboardRemove())
    await temp.delete()
    await message.answer("Please select your language:", reply_markup = keyboards.startMarkup)


async def textchecker(text, maxlength=800):
    if len(text) > maxlength:
        return False
    return True
