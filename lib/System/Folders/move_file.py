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
from config import ALLOWED_USER_ID
from lib.states import move_file

import shutil
import os

def register_move_file(dp):
    @dp.message(F.text.lower() == "перемeстить файл")
    @dp.message(Command("move_file"))
    async def start_move_file(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer(
                "Хорошо, введите путь файла, который хотите переместить (например, C:/Users/Public/Название_файла.txt):")
            await state.set_state(move_file.waiting_path1)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    @dp.message(move_file.waiting_path1)
    async def get_source_path(message: types.Message, state: FSMContext):
        source_path = message.text

        # Проверка, существует ли исходный файл
        if not os.path.isfile(source_path):
            await message.answer("Файл не найден. Пожалуйста, убедитесь, что путь к файлу указан правильно и перезапустите процесс.")
            await state.clear()
            return  # Прерываем дальнейшее выполнение

        await state.update_data(source_path=source_path)
        await message.answer("Теперь введите путь, куда нужно переместить файл (например, C:/Users/Public/Целевая_папка/):")
        await state.set_state(move_file.waiting_path2)

    @dp.message(move_file.waiting_path2)
    async def get_destination_path(message: types.Message, state: FSMContext):
        destination_path = message.text
        data = await state.get_data()
        source_path = data.get("source_path")

        # Проверка, существует ли директория назначения
        if not os.path.isdir(destination_path):
            await message.answer("Целевая директория не найдена. Пожалуйста, убедитесь, что путь к директории указан правильно и перезапустите процесс.")
            await state.clear()
            return  # Прерываем дальнейшее выполнение

        try:
            # Попытка перемещения файла
            shutil.move(source_path, destination_path)
            await message.answer(f"Файл успешно перемещён в {destination_path}.")
        except FileNotFoundError:
            await message.answer("Файл или директория не найдены. Проверьте путь.")
        except PermissionError:
            await message.answer("Недостаточно прав для перемещения файла. Пожалуйста, проверьте права доступа.")
        except OSError as e:
            await message.answer(f"Ошибка доступа к файлу или директории: {e}")
        except Exception as e:
            await message.answer(f"Произошла непредвиденная ошибка: {e}")
        finally:
            await state.clear()