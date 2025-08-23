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
from config import ALLOWED_USER_ID, bot, MAX_ATTEMPTS
from lib.states import DirectoryStateSaveFiles
from aiogram.types import ContentType
from lib.texts import TEXTS, user_languages

import os 

def register_load_file(dp):
    @dp.message(F.text.lower().in_(["загрузить файл", "upload file"]))
    @dp.message(Command("upload_file"))
    async def handle_text_message(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['ask_upload_path'])
            await state.set_state(DirectoryStateSaveFiles.waiting_for_directory_saveFiles)
            await state.update_data(attempts=0)
        else:
            await message.answer(TEXTS[lang]['no_access'])

    @dp.message(DirectoryStateSaveFiles.waiting_for_directory_saveFiles)
    async def set_new_directory(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            directory = message.text
            data = await state.get_data()
            attempts = data.get('attempts', 0)

            if not directory or not os.path.isdir(directory):
                attempts += 1
                if attempts >= MAX_ATTEMPTS:
                    await message.answer(TEXTS[lang]['upload_invalid_path_final'])
                    await state.clear()
                else:
                    await state.update_data(attempts=attempts)
                    await message.answer(TEXTS[lang]['upload_invalid_path'])
            else:
                await state.update_data(directoryForSaveFiles=directory, attempts=0)
                await message.answer(TEXTS[lang]['upload_ready'].format(path=directory))
                await state.set_state(DirectoryStateSaveFiles.waiting_for_files)
        else:
            await message.answer(TEXTS[lang]['no_access'])

    @dp.message(DirectoryStateSaveFiles.waiting_for_files, F.content_type.in_([ContentType.PHOTO, ContentType.DOCUMENT, ContentType.AUDIO]))
    async def handle_document_or_audio(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['no_access'])
            return

        user_data = await state.get_data()
        directory = user_data.get('directoryForSaveFiles')

        if not directory or not os.path.isdir(directory):
            await message.reply(TEXTS[lang]['upload_missing_path'])
            await state.clear()
            return

        if message.document:
            document = message.document
            file_id = document.file_id
            file_name = document.file_name or "document.bin"
        elif message.photo:
            document = message.photo[-1]
            file_id = document.file_id
            file_name = "photo.jpg"
        elif message.audio:
            document = message.audio
            file_id = document.file_id
            file_name = document.file_name or "audio.mp3"
        else:
            await message.reply(TEXTS[lang]['upload_no_supported_file'])
            return

        try:
            await message.reply(TEXTS[lang]['upload_saving'])
            file_info = await bot.get_file(file_id)
            file_path = file_info.file_path

            file = await bot.download_file(file_path)
            save_path = os.path.join(directory, file_name)

            with open(save_path, 'wb') as f:
                f.write(file.read())

            await message.reply(TEXTS[lang]['upload_success'].format(name=file_name, path=directory))
        except Exception as e:
            await message.reply(TEXTS[lang]['upload_error'].format(error=e))
        finally:
            await state.clear()