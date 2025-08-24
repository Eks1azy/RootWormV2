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


import os
import ctypes
from aiogram import types, F
from aiogram.filters import Command
from aiogram.types import ContentType
from aiogram.fsm.context import FSMContext
from config import ALLOWED_USER_ID, directory
from config import bot
from lib.states import fdesk
from lib.texts import TEXTS, user_languages

def register_wallpaper_handlers(dp):
    @dp.message(F.text.lower() == "поменять обои")
    @dp.message(F.text.lower() == "change wallpaper")
    @dp.message(Command("change_wallpaper"))
    async def wallpaper_start(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['send_photo'])
            await state.set_state(fdesk.waiting_photo)
        else:
            await message.answer(TEXTS[lang]['access_denied'])

    @dp.message(fdesk.waiting_photo, F.content_type.in_([ContentType.PHOTO, ContentType.DOCUMENT]))
    async def wallpaper_receive(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['access_denied'])
            return

        try:
            # Определяем имя файла
            if message.content_type == ContentType.PHOTO:
                file_id = message.photo[-1].file_id
                file_name = f"{file_id}.jpg"
            else:
                file_id = message.document.file_id
                file_name = message.document.file_name

            file_info = await bot.get_file(file_id)
            file_path = file_info.file_path
            file = await bot.download_file(file_path)

            save_path = os.path.join(directory, file_name)
            os.makedirs(directory, exist_ok=True)

            with open(save_path, "wb") as f:
                f.write(file.getvalue())

            # Устанавливаем обои
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(save_path), 3)

            await message.reply(TEXTS[lang]['wallpaper_changed'])

            os.remove(save_path)
            await state.clear()

        except FileNotFoundError:
            await message.reply(TEXTS[lang]['file_not_found'])
        except Exception as e:
            await message.reply(TEXTS[lang]['error_occurred'].format(error=e))