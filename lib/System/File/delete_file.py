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


# from library import *
from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from config import ALLOWED_USER_ID
from lib.states import waitmas
from lib.texts import TEXTS, user_languages
from lib.states import logger

import os 

def register_delete_file(dp):
    @dp.message(F.text.lower().in_(["удалить файл", "delete file"]))
    @dp.message(Command("delete_file"))
    async def send_file(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['ask_delete_path'])
            await state.set_state(waitmas.file_name_delet)
        else:
            await message.answer(TEXTS[lang]['no_access'])

    @dp.message(waitmas.file_name_delet)
    async def process_send_file(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            file_path = message.text

            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    await message.answer(TEXTS[lang]['file_deleted'].format(path=file_path))
                except Exception as e:
                    logger.error(f"Ошибка при удалении файла {file_path}: {e}")
                    await message.answer(TEXTS[lang]['delete_error'].format(path=file_path))
            else:
                await message.answer(TEXTS[lang]['file_not_found'].format(path=file_path))

            await state.clear()
        else:
            await message.answer(TEXTS[lang]['no_access'])