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
from lib.states import Form
from lib.texts import TEXTS, user_languages

import os

def register_create_folder(dp):
    @dp.message(F.text.lower().in_({"создать папку", "create folder"}))
    @dp.message(Command("create_folder"))
    async def create_folder_command(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['create_folder_prompt'])
            await state.set_state(Form.folder_name)
        else:
            await message.answer(TEXTS[lang]['no_access'])

    @dp.message(Form.folder_name)
    async def process_folder_name(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            folder_name = message.text

            if os.path.dirname(folder_name):
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name, exist_ok=True)
                    await message.answer(TEXTS[lang]['folder_created'].format(folder_name=folder_name))
                    await state.clear()
                else:
                    await message.answer(TEXTS[lang]['folder_exists'].format(folder_name=folder_name))
                    await state.clear()
            else:
                await message.answer(TEXTS[lang]['folder_invalid_path'])
                await message.answer(TEXTS[lang]['try_again'])
                await state.clear()
        else:
            await message.answer(TEXTS[lang]['no_access'])