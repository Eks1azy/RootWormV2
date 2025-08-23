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
from aiogram.types import FSInputFile
from config import ALLOWED_USER_ID
from lib.states import waitingfile
from lib.texts import TEXTS, user_languages

import os

def register_download_file(dp):
    @dp.message(F.text.lower().in_(["скачать файл", "download file"]))
    @dp.message(Command("send_file"))
    async def send_file(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['ask_download_path'])
            await state.set_state(waitingfile.file_name_send)
        else:
            await message.answer(TEXTS[lang]['no_access'])

    @dp.message(waitingfile.file_name_send)
    async def process_send_file(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            file_path = message.text

            try:
                if not os.path.isfile(file_path):
                    await message.answer(TEXTS[lang]['file_not_found'].format(path=file_path))
                    await state.clear()
                    return

                file_size = os.path.getsize(file_path)
                max_size = 50 * 1024 * 1024  # 50 MB

                if file_size > max_size:
                    await message.answer(TEXTS[lang]['file_too_large'].format(size=file_size / (1024 * 1024)))
                    await state.clear()
                    return

                document = FSInputFile(file_path)
                await message.answer_document(document)
            except Exception as e:
                await message.answer(TEXTS[lang]['send_file_error'].format(error=e))
            finally:
                await state.clear()
        else:
            await message.answer(TEXTS[lang]['no_access'])