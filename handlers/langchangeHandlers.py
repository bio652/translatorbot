from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from data import data
from kbs import keyboards
from states import states
from messages import messages
from . import someMethods
from translator import maintranslator

langrt = Router()

async def findkey(message):
    newkey = None
    for key, values in maintranslator.LANGUAGES_TRANSLATED.items():
            if any(message == value for value in values.values()):
                newkey = key
                break 
    return newkey

@langrt.callback_query(F.data == "srcl")
async def srcl(callback: types.CallbackQuery, state: FSMContext):
    if data.checkUser(userid=callback.from_user.id):
        await callback.message.delete()
        await state.set_state(states.Src.srclang)
        mainl = int(data.getUserlang(callback.from_user.id))
        await callback.message.answer(messages.SRCMESSAGE[mainl], reply_markup=await keyboards.langMarkup(mainl))


@langrt.message(states.Src.srclang)
async def srcupdate(message: types.Message, state: FSMContext):
    if data.checkUser(userid=message.from_user.id):
        if message.text in messages.BACKKB.values():
            await backmes(message, state)
            return
        mainl = int(data.getUserlang(message.from_user.id))
        newkey = await findkey(message.text)
        if newkey is None: 
            await message.answer(messages.SRCWRMESSAGE[mainl])
        elif newkey == data.getTranslangs(message.from_user.id)[0]:
            print("same")
            await someMethods.mainmenu(message,state)
        else:
            result = data.trlangupdate(userid=message.from_user.id,newlang=newkey)
            if result:
                await message.answer(messages.SRCSUCCESS[mainl], reply_markup=keyboards.ReplyKeyboardRemove())
                await someMethods.mainmenu(message,state)
            else:
                await state.clear()
                await message.answer("Error :(\nPlease write - /start")
    
    
@langrt.callback_query(F.data == "destl")
async def destl(callback: types.CallbackQuery, state: FSMContext):
    if data.checkUser(userid=callback.from_user.id):
        await callback.message.delete()
        await state.set_state(states.Dest.destlang)
        mainl = int(data.getUserlang(callback.from_user.id))
        await callback.message.answer(messages.DESTMESSAGE[mainl], reply_markup=await keyboards.langMarkup(mainl))
        
@langrt.message(states.Dest.destlang)
async def srcupdate(message: types.Message, state: FSMContext):
    if data.checkUser(userid=message.from_user.id):
        if message.text in messages.BACKKB.values():
            await backmes(message, state)
            return
        mainl = int(data.getUserlang(message.from_user.id))
        newkey = await findkey(message.text)
        if newkey is None: 
            await message.answer(messages.DESTWRMESSAGE[mainl])
        elif newkey == data.getTranslangs(message.from_user.id)[1]:
            print("same")
            await someMethods.mainmenu(message,state)
        else:
            result = data.tolangupdate(userid=message.from_user.id,newlang=newkey)
            if result:
                await message.answer(messages.DESTSUCCESS[mainl], reply_markup=keyboards.ReplyKeyboardRemove())
                await someMethods.mainmenu(message,state)
            else:
                await state.clear()
                await message.answer("Error :(\nPlease write - /start")
    
@langrt.callback_query(F.data == "back")
async def back(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    await someMethods.mainmenucb(callback, state)
    
async def backmes(message: types.Message, state: FSMContext):
    await someMethods.mainmenu(message, state)