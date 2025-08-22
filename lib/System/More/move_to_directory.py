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
from lib.states import DirectoryState, current_directory
from config import ALLOWED_USER_ID
import os


def register_cd(dp):
    @dp.message(F.text == "Переместиться по директории [ Просмотр папок ]")
    @dp.message(Command("change_directory"))
    async def change_directory(message: types.Message, state: FSMContext):
        await message.answer("Введите путь к директории для просмотра файлов (или 'exit' для выхода):")
        await state.set_state(DirectoryState.waiting_for_directory)

    @dp.message(DirectoryState.waiting_for_directory)
    async def set_new_directory(message: types.Message, state: FSMContext):
        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
            return

        user_input = message.text.strip()

        if user_input.lower() == "exit":
            await message.answer("Выход из режима перемещения по директориям.")
            await state.clear()
            return

        global current_directory
        new_directory = user_input

        if os.path.isdir(new_directory):
            current_directory = new_directory
            await message.answer(f"Перемещено root. Текущая директория:\n{current_directory}")

            try:
                folders = [
                    name for name in os.listdir(current_directory)
                    if os.path.isdir(os.path.join(current_directory, name))
                ]
                if folders:
                    folder_list = "\n".join(folders)
                    await message.answer(f"Папки в текущей директории:\n{folder_list}")
                else:
                    await message.answer("В этой директории нет папок.")
            except Exception as e:
                await message.answer(f"Ошибка при получении списка папок:\n{e}")
        else:
            await message.answer("Неверный путь. Попробуйте снова root.")

        await message.answer("Введите путь к следующей директории (или 'exit' для выхода):")

    tasks = {}
