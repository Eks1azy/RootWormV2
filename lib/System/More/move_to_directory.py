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
from config import ALLOWED_USER_ID
from lib.states import DirectoryState, current_directory

import os

def register_cd(dp):
    @dp.message(F.text == "Переместиться по директории")
    @dp.message(Command("change_directory"))
    async def change_directory(message: types.Message, state: FSMContext):
        await message.answer("Введите путь к новой директории:")
        await state.set_state(DirectoryState.waiting_for_directory)

    # Обработчик для ввода новой директории
    @dp.message(DirectoryState.waiting_for_directory)
    async def set_new_directory(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            global current_directory
            new_directory = message.text

            if os.path.isdir(new_directory):
                current_directory = new_directory
                await message.answer(f"Успешно переместился, вот текущая директория:\n{current_directory}")
            else:
                await message.answer("Неверный путь. Попробуйте снов.")

            await state.clear()
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
    tasks = {}
