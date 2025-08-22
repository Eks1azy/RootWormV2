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
from lib.states import Form

import os

def register_create_folder(dp):
    @dp.message(F.text.lower() == "создать папку")
    @dp.message(Command("create_folder"))
    async def create_folder_command(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer(
                "Укажите путь где создать папку и вконце название папки, пример:\n C:/Users/Public/Название_папки")
            await state.set_state(Form.folder_name)  # Переходим в состояние ожидания имени папки

        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    @dp.message(Form.folder_name)
    async def process_folder_name(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            folder_name = message.text

            # Проверяем, содержит ли введенный текст полный путь (например, наличие "/")
            if os.path.dirname(folder_name):  # Если есть путь
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name, exist_ok=True)  # Создаем папку
                    await message.answer(f"Папка '{folder_name}' успешно создана!")
                    await state.clear()  # Сброс состояния после успешного завершения
                else:
                    await message.answer(f"Папка с именем '{folder_name}' уже существует!")
                    await state.clear()  # Сброс состояния после успешного завершения
            else:  # Если введено только название без пути
                await message.answer("Пожалуйста, укажите полный путь к папке, а не только её название.")
                # Перезапускаем процесс создания папки
                await message.answer("Попробуйте снова. Перезапустив процесс.")
                await state.clear()  # Сброс состояния после успешного завершения


        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")