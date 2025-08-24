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
from config import ALLOWED_USER_ID
from lib.states import DirectoryState, current_directory
from lib.texts import TEXTS, user_languages

import os

def register_cd(dp):
    @dp.message(F.text == "Переместиться по директории")
    @dp.message(F.text == "Change directory")
    @dp.message(Command("change_directory"))
    async def change_directory(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        await message.answer(TEXTS[lang]['enter_new_directory'])
        await state.set_state(DirectoryState.waiting_for_directory)

    # Обработчик для ввода новой директории
    @dp.message(DirectoryState.waiting_for_directory)
    async def set_new_directory(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id == ALLOWED_USER_ID:
            global current_directory
            new_directory = message.text

            if os.path.isdir(new_directory):
                current_directory = new_directory
                await message.answer(f"{TEXTS[lang]['directory_changed']}:\n{current_directory}")
            else:
                await message.answer(TEXTS[lang]['invalid_directory'])

            await state.clear()
        else:
            await message.answer(TEXTS[lang]['access_denied'])
    tasks = {}