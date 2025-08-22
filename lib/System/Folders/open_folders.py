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
from lib.states import Openfile
from config import ALLOWED_USER_ID, MAX_MESSAGE_LENGTH, MAX_ATTEMPTS

import os

def register_open_file_handlers(dp):
    @dp.message(F.text.lower() == "открыть файл")
    @dp.message(Command("open_file"))
    async def cmd_start(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer(
                "Укажите путь и имя файла с его расширением, пример:\n C:/Users/Public/Название_файла.txt"
            )
            await state.set_state(Openfile.waiting_for_dfile)  # Переход в состояние ожидания пути файла

        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    @dp.message(Openfile.waiting_for_dfile)
    async def web_record_send(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            directoryopn = message.text

            # Проверка существования файла
            if os.path.isfile(directoryopn):
                try:
                    # Запуск .exe или .bat файла на Windows
                    os.system(f'start "" "{directoryopn}"')
                    await message.answer("Файл был успешно открыт.")
                except Exception as e:
                    await message.answer(f"Произошла ошибка при открытии файла: {e}")
            else:
                await message.answer(f"Файл {directoryopn} не был найден. \nПожалуйста, проверьте правильность пути и имени файла, затем повторите попытку.")

            await state.clear()  

        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
    