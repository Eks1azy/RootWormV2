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
from aiogram import types
from config import ALLOWED_USER_ID
from lib.states import waiting
from lib.texts import TEXTS, user_languages

import shutil
import os

def register_folder_delete(dp):
    @dp.message(F.text.lower().in_({"удалить папку", "delete folder"}))
    @dp.message(Command("delete_folder"))
    async def delet_folder_command(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['delete_folder_prompt'])
            await state.set_state(waiting.folder_name_delet)
        else:
            await message.answer(TEXTS[lang]['no_access'])

    # Incorrect attempts tracking
    incorrect_attempts = {}

    @dp.message(waiting.folder_name_delet)
    async def processdelet_folder_name(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')
        folder_name_delet = message.text

        if user_id not in incorrect_attempts:
            incorrect_attempts[user_id] = 0

        if user_id == ALLOWED_USER_ID:
            if os.path.exists(folder_name_delet) and os.path.isdir(folder_name_delet):
                try:
                    shutil.rmtree(folder_name_delet)
                    await message.answer(TEXTS[lang]['folder_deleted'].format(folder_name=folder_name_delet))
                    await state.clear()
                    incorrect_attempts[user_id] = 0
                except Exception as e:
                    await message.answer(TEXTS[lang]['folder_delete_error'].format(error=e))
                    await state.clear()
            else:
                incorrect_attempts[user_id] += 1
                if incorrect_attempts[user_id] >= 1:
                    await message.answer(TEXTS[lang]['folder_not_found'].format(folder_name=folder_name_delet))
                    await message.answer(TEXTS[lang]['try_again'])
                    await state.clear()
        else:
            await message.answer(TEXTS[lang]['no_access'])