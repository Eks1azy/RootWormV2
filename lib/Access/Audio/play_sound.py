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


from lib.states import SoundStates
from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from playsound import playsound
from lib.texts import TEXTS, user_languages

import os
import threading

from config import ALLOWED_USER_ID

def register_play_sound_handlers(dp):
    @dp.message(F.text.lower().in_({"воспроизвести звук", "play sound"}))
    @dp.message(Command("play_sound"))
    async def start_getting_path(message: types.Message, state: FSMContext):
        user_id = message.from_user.id

        # Определяем язык по кнопке или из user_languages
        if message.text.lower() == "воспроизвести звук":
            lang = 'ru'
        else:
            lang = user_languages.get(user_id, 'en')

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang].get("access_denied", "You do not have access to this command."))
            return

        await message.answer(TEXTS[lang].get(
            "enter_mp3_path",
            "Enter the full path to the MP3 file (e.g., `/home/user/music/mysound.mp3`):"
        ))
        await state.set_state(SoundStates.waiting_for_file_path)

    @dp.message(SoundStates.waiting_for_file_path)
    async def play_sound(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id != ALLOWED_USER_ID:
            await state.clear()
            return

        file_path = message.text.strip()

        if not os.path.isfile(file_path) or not file_path.lower().endswith(".mp3"):
            await message.answer(TEXTS[lang].get(
                "invalid_mp3",
                "The file does not exist or is not an MP3. Try again with the command."
            ))
            await state.clear()
            return

        try:
            threading.Thread(target=playsound, args=(file_path,), daemon=True).start()
            await message.answer(TEXTS[lang].get("playing_sound", "The sound is playing, root!"))
        except Exception as e:
            await message.answer(TEXTS[lang].get("play_error", f"Error playing file: {e}"))

        await state.clear()