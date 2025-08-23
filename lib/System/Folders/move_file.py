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
from lib.states import move_file
from lib.texts import TEXTS, user_languages

import shutil
import os

def register_move_file(dp):
    @dp.message(F.text.lower().in_({"перемистить файл", "move file"}))
    @dp.message(Command("move_file"))
    async def start_move_file(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['move_file_prompt_source'])
            await state.set_state(move_file.waiting_path1)
        else:
            await message.answer(TEXTS[lang]['no_access'])

    @dp.message(move_file.waiting_path1)
    async def get_source_path(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')
        source_path = message.text

        if not os.path.isfile(source_path):
            await message.answer(TEXTS[lang]['move_file_not_found'])
            await state.clear()
            return

        await state.update_data(source_path=source_path)
        await message.answer(TEXTS[lang]['move_file_prompt_dest'])
        await state.set_state(move_file.waiting_path2)

    @dp.message(move_file.waiting_path2)
    async def get_destination_path(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')
        destination_path = message.text
        data = await state.get_data()
        source_path = data.get("source_path")

        if not os.path.isdir(destination_path):
            await message.answer(TEXTS[lang]['move_dir_not_found'])
            await state.clear()
            return

        try:
            shutil.move(source_path, destination_path)
            await message.answer(TEXTS[lang]['move_file_success'].format(destination_path=destination_path))
        except FileNotFoundError:
            await message.answer(TEXTS[lang]['move_file_not_found'])
        except PermissionError:
            await message.answer(TEXTS[lang]['move_file_no_permission'])
        except OSError as e:
            await message.answer(TEXTS[lang]['move_file_os_error'].format(error=e))
        except Exception as e:
            await message.answer(TEXTS[lang]['move_file_unknown_error'].format(error=e))
        finally:
            await state.clear()