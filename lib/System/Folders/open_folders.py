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
from lib.states import Openfile
from config import ALLOWED_USER_ID
from lib.texts import TEXTS, user_languages

import os

def register_open_file_handlers(dp):
    @dp.message(F.text.lower().in_({"открыть файл", "open file"}))
    @dp.message(Command("open_file"))
    async def cmd_start(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['open_file_prompt'])
            await state.set_state(Openfile.waiting_for_dfile)
        else:
            await message.answer(TEXTS[lang]['no_access'])

    @dp.message(Openfile.waiting_for_dfile)
    async def open_file(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')
        file_path = message.text

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['no_access'])
            return

        if os.path.isfile(file_path):
            try:
                os.system(f'start "" "{file_path}"')
                await message.answer(TEXTS[lang]['open_file_success'])
            except Exception as e:
                await message.answer(TEXTS[lang]['open_file_error'].format(error=e))
        else:
            await message.answer(TEXTS[lang]['open_file_not_found'].format(file_path=file_path))

        await state.clear()