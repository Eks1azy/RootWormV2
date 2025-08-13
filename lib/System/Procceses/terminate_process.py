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


from lib.states import ProcessState
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import types, F
import psutil
from lib.states import Form
from config import ALLOWED_USER_ID


def register_terminate_process_handlers(dp):
    @dp.message(F.text.lower() == "завершить процесс")
    @dp.message(Command("terminate_process"))
    async def cmd_andprocesses(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer("Укажите PID процесса.")
            await state.set_state(ProcessState.waiting_for_pid)  # Устанавливаем состояние ожидания PID
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    # Обработчик для получения PID от пользователя
    @dp.message(ProcessState.waiting_for_pid)
    async def process_pid(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            user_input = message.text

            # Проверка, является ли введенное значение числом
            if not user_input.isdigit():
                await message.answer(f"{user_input} - Не является PID.")
                await state.clear()  # Завершаем состояние
                return

            pid = int(user_input)  # Преобразуем строку в числоw

            try:
                process = psutil.Process(pid)
                process.terminate()  # Попробовать мягко завершить процесс
                process.wait(timeout=3)  # Подождать завершения процесса
                await message.answer(f"Процесс с PID {pid} успешно завершен.")
            except psutil.NoSuchProcess:
                await message.answer(f"Процесс с PID {pid} не найден.")
            except psutil.AccessDenied:
                await message.answer(f"Недостаточно прав для завершения процесса с PID {pid}.")
            except psutil.TimeoutExpired:
                await message.answer(f"Процесс с PID {pid} не завершился за отведенное время. Принудительное завершение.")
                process.kill()  # Принудительное завершение процесса
                await message.answer(f"Процесс с PID {pid} принудительно завершен.")
            # Завершаем состояние после успешной обработки
            await state.clear()
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")