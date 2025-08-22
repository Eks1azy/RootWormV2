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



# from library import *
from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from config import ALLOWED_USER_ID
from lib.states import waitmas

import os 

def register_delete_file(dp):
    @dp.message(F.text.lower() == "удалить файл")
    @dp.message(Command("delete_file"))
    async def send_file(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer(
                "Укажите путь и расширение файла которого хотите удалить, пример:\n C:/Users/Public/Название_файла.txt")
            await state.set_state(waitmas.file_name_delet)  # Переходим в состояние ожидания имени папки

        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")


    @dp.message(waitmas.file_name_delet)
    async def process_send_file(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            directory_file_delet = message.text  # Путь к файлу
            # Проверяем, существует ли файл
            if os.path.exists(directory_file_delet):
                os.remove(directory_file_delet)  # Удаляем файл
                await message.answer(f"Файл '{directory_file_delet}' успешно удален.")
            else:
                await message.answer(f"Файл '{directory_file_delet}' не был найден. \nПожалуйста, проверьте правильность пути и имени файла, затем повторите попытку.")
            await state.clear()  # Завершаем состояние (aiogram 3.x)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
