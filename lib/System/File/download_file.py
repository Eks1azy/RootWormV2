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
from config import ALLOWED_USER_ID
from lib.states import waitingfile

import os

def register_download_file(dp):
    @dp.message(F.text.lower() == "скачать файл")
    @dp.message(Command("send_file"))
    async def send_file(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer(
                "Укажите путь и расширение файла, пример:\n C:/Users/Public/Название_файла.txt"
            )
            await state.set_state(waitingfile.file_name_send)  # Переход в состояние ожидания пути файла
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    @dp.message(waitingfile.file_name_send)
    async def process_send_file(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            directory_file = message.text  # Путь к файлу

            try:
                # Проверка наличия файла
                if not os.path.isfile(directory_file):
                    await message.answer("Файл не найден. Проверьте путь и попробуйте снова.")
                    await state.clear()  # Сброс состояния
                    return

                # Проверка размера файла
                file_size = os.path.getsize(directory_file)
                max_size = 50 * 1024 * 1024  # 50 MB

                if file_size > max_size:
                    await message.answer(f"Файл слишком большой ({file_size / (1024 * 1024):.2f} MB). Максимальный размер файла - 50 MB.")
                    await state.clear()  # Сброс состояния
                    return  # Завершаем выполнение функции, чтобы не продолжать обработку

                # Создание объекта для отправки
                document = FSInputFile(directory_file)

                # Отправка файла пользователю
                await message.answer_document(document)
                await state.clear()  # Сброс состояния
            except Exception as e:
                await message.answer(f"Произошла ошибка: {e}\n")
                await state.clear()  # Сброс состояния
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")