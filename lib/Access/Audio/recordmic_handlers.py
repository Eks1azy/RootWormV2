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
from lib.texts import TEXTS, user_languages

class microfonetime(StatesGroup):
    waiting_for_microtime = State()
    waiting_for_retry = State()  




def register_audio_handlers(dp):
    @dp.message(F.text.lower().in_({"запись аудио", "audio record"}))
    @dp.message(Command("audio_record"))
    async def audio_record(message: types.Message, state: FSMContext):
        lang = user_languages.get(message.from_user.id, 'en')
        texts = TEXTS[lang]
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer(texts['ask_duration'])
            await state.set_state(microfonetime.waiting_for_microtime)
        else:
            await message.answer(texts['no_access'])

    @dp.message(microfonetime.waiting_for_microtime)
    async def process_audio_time_input(message: types.Message, state: FSMContext):
        lang = user_languages.get(message.from_user.id, 'en')
        texts = TEXTS[lang]

        if message.from_user.id == ALLOWED_USER_ID:
            try:
                recording_time = int(message.text)
                await start_audio_recording(message, state, recording_time)
            except ValueError:
                await message.answer(texts['invalid'])
                await state.clear()
        else:
            await message.answer(texts['no_access'])