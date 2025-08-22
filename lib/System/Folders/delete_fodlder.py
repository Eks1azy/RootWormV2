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
from aiogram import types
from config import ALLOWED_USER_ID
from lib.states import waiting

import shutil
import os

def register_folder_delete(dp):
    @dp.message(F.text.lower() == "удалить папку")
    @dp.message(Command("delete_folder"))
    async def delet_folder_command(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer(
                "Укажите путь и вконце название папки, пример:\n C:/Users/Public/Название_папки\n!!!Папка удаляется со всем содержимым!!!")
            await state.set_state(waiting.folder_name_delet)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")


    # Словарь для хранения количества некорректных вводов
    incorrect_attempts = {}
    @dp.message(waiting.folder_name_delet)
    async def processdelet_folder_name(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        folder_name_delet = message.text

        # Инициализация счётчика некорректных вводов для пользователя
        if user_id not in incorrect_attempts:
            incorrect_attempts[user_id] = 0

        if message.from_user.id == ALLOWED_USER_ID:
            # Проверяем, существует ли папка
            if os.path.exists(folder_name_delet) and os.path.isdir(folder_name_delet):
                try:
                    shutil.rmtree(folder_name_delet)
                    await message.answer(f"Папка '{folder_name_delet}' и все её содержимое успешно удалены.")
                    # Завершаем состояние после успешного удаления
                    await state.set_state(None)
                    # Сбрасываем счётчик некорректных вводов
                    incorrect_attempts[user_id] = 0
                except Exception as e:
                    await message.answer(f"Ошибка при удалении папки: {e}")
                    # Завершаем состояние при критической ошибке
                    await state.set_state(None)
            else:
                incorrect_attempts[user_id] += 1
                if incorrect_attempts[user_id] >= 1:
                    await message.answer(f"Папка '{folder_name_delet}' не найдена. Пожалуйста, введите корректный путь к папке")
                    await message.answer("Попробуйте снова. Перезапустив процесс.")
                    await state.clear()

        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
