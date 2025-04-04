from aiogram.fsm.state import StatesGroup, State

class Start(StatesGroup):
    langselect = State()
    
class Src(StatesGroup):
    srclang = State()
    
class Dest(StatesGroup):
    destlang = State()