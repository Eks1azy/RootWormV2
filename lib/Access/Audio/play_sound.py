##  _________________________________________
##   |_______  authors: Eks1azy     _______|
##    \_\_\_|______  Oqwe4O  _______|\_\_\_\
##    \_\_\_|______  Tusay1  _______|\_\_\_\
##           \_\_\_\_\_\_\_\_\_\_\_\
##   ___________________________________________
##  |                                          /\
##  |  github:https://github.com/Eks1azy      / /
##  |                                        / /
##  |    if you will find some bugs or      / /
##  |                                      / /
##  |    have ideas for improvements,     / /
##  |                                    / /
##  |       please send it to me        / /
##  |__________________________________/ /
##  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/



from lib.states import SoundStates
from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from playsound import playsound

import os
import threading

from config import ALLOWED_USER_ID

def register_play_sound_handlers(dp):
    @dp.message(F.text.casefold().startswith("воспроизвести звук"))
    @dp.message(Command("play_sound"))
    async def start_getting_path(message: types.Message, state: FSMContext):
        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer("У вас нет доступа к этой команде.")
            return

        await message.answer("Введите полный путь к MP3-файлу (например: `/home/user/music/mysound.mp3`):")
        await state.set_state(SoundStates.waiting_for_file_path)

    @dp.message(SoundStates.waiting_for_file_path)
    async def play_sound(message: types.Message, state: FSMContext):
        if message.from_user.id != ALLOWED_USER_ID:
            await state.clear()
            return

        file_path = message.text.strip()

        if not os.path.isfile(file_path) or not file_path.lower().endswith(".mp3"):
            await message.answer("Файл не существует или это не MP3-файл. Попробуйте снова через команду.")
            await state.clear()
            return

        try:
            threading.Thread(target=playsound, args=(file_path,), daemon=True).start()
            await message.answer("Звук воспроизводится, root!")
        except Exception as e:
            await message.answer(f"Ошибка воспроизведения: {e}")

        await state.clear()