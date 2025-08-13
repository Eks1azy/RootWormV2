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

def register_wallpaper_handlers(dp):
    @dp.message(F.text.lower() == "поменять обои")
    @dp.message(Command("change_wallpaper"))
    async def wallpaper(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer("Хорошо, отправьте фото.")
            await state.set_state(fdesk.waiting_photo)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    @dp.message(fdesk.waiting_photo, F.content_type.in_([ContentType.PHOTO, ContentType.DOCUMENT]))
    async def receiving_photo(message: types.Message, state: FSMContext):
        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
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

            with open(save_path, "wb") as f:
                f.write(file.getvalue())

            # Устанавливаем обои
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(save_path), 3)

            await message.reply("Обои успешно заменены.")

            os.remove(save_path)
            await state.clear()

        except FileNotFoundError:
            await message.reply("Ошибка: файл не найден.")
        except Exception as e:
            await message.reply(f"Произошла ошибка: {e}")