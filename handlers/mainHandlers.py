from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from data import data
from kbs import keyboards
from states import states
from messages import messages
from . import someMethods
from translator import maintranslator

mainrt = Router()


@mainrt.message(Command('start'))
async def start(message: types.message, state: FSMContext):
    if data.checkUser(userid=message.from_user.id):
        await state.clear()
        await someMethods.mainmenu(message, state)
    else:
        await state.set_state(states.Start.langselect)
        await message.answer("Hi! Please select your language:", reply_markup = keyboards.startMarkup)

@mainrt.callback_query(states.Start.langselect)
async def langselect(callback: types.CallbackQuery, state: FSMContext):
    if data.checkUser(userid=callback.from_user.id):
        if callback.data in ["0","1","2"]:
            result = data.updatemenulang(userid=callback.from_user.id, userlang=callback.data)
        else:
            await state.clear()
            mainl = int(data.getUserlang(userid=callback.from_user.id))
            await callback.message.answer(messages.ERRORMESSAGE[mainl])
            await someMethods.mainmenucb(callback, state)
            return
    else:
        result = data.addUser(userid=callback.from_user.id, userlang=callback.data)

    if result:
        await state.clear()
        await callback.answer(messages.AFTERLANGSEL[int(callback.data)])
        await callback.message.delete()
        await someMethods.mainmenucb(callback, state)
        
@mainrt.message(F.text.in_(sum(messages.MAINKB.values(), [])))
async def mainkbroot(message: types.Message, state: FSMContext):
    if data.checkUser(userid=message.from_user.id):
        for lang_index, buttons in messages.MAINKB.items():
            if message.text in buttons:
                button_index = buttons.index(message.text)
                if button_index == 0:  # "Change languages for translation"
                    temp = await message.answer(".", reply_markup=keyboards.ReplyKeyboardRemove())
                    await changelanguages(message, state)
                    await temp.delete()
                    break
                elif button_index == 1:  # "Change menu language"
                    await someMethods.changemenulang(message, state)                    
                    break
    else:
        await start(message, state)
  
async def changelanguages(message: types.Message, state: FSMContext):
    if data.checkUser(userid=message.from_user.id):
        mainl = int(data.getUserlang(message.from_user.id))
        langs = data.getTranslangs(userid=message.from_user.id)
        await message.answer(messages.CANGELANGS[mainl], reply_markup=await keyboards.changeMarkup(mainl))
    else:
        await start(message, state)

    
@mainrt.message(default_state)
async def translation(message: types.Message, state: FSMContext):
    if data.checkUser(userid=message.from_user.id):
        mainl = int(data.getUserlang(message.from_user.id))
        langs = data.getTranslangs(userid=message.from_user.id)
        if await someMethods.textchecker(message.text):
            print(langs[0], langs[1])
            transl = maintranslator.translator.translate(str(message.text), src=langs[0], dest=langs[1]).text
            await message.answer(messages.TRMESSAGE[mainl].format(transl = transl))
        else:
            await message.answer(messages.ERRORMESSAGE[mainl])
    else:
        await start(message, state)
        