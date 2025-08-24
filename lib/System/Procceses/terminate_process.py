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
from lib.texts import TEXTS, user_languages


def register_terminate_process_handlers(dp):
    @dp.message(F.text.lower() == "завершить процесс")
    @dp.message(F.text.lower() == "terminate process")
    @dp.message(Command("terminate_process"))
    async def cmd_andprocesses(message: types.Message, state: FSMContext):
        lang = user_languages.get(message.from_user.id, 'ru')
        t = TEXTS[lang]

        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer(t["no_access"])
            return

        await message.answer(t["enter_pid"])
        await state.set_state(ProcessState.waiting_for_pid)

    @dp.message(ProcessState.waiting_for_pid)
    async def process_pid(message: types.Message, state: FSMContext):
        lang = user_languages.get(message.from_user.id, 'ru')
        t = TEXTS[lang]

        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer(t["no_access"])
            return

        user_input = message.text

        if not user_input.isdigit():
            await message.answer(t["invalid_pid"].format(pid=user_input))
            await state.clear()
            return

        pid = int(user_input)

        try:
            process = psutil.Process(pid)
            process.terminate()
            process.wait(timeout=3)
            await message.answer(t["process_terminated"].format(pid=pid))
        except psutil.NoSuchProcess:
            await message.answer(t["process_not_found"].format(pid=pid))
        except psutil.AccessDenied:
            await message.answer(t["access_denied"].format(pid=pid))
        except psutil.TimeoutExpired:
            await message.answer(t["terminate_timeout"].format(pid=pid))
            process.kill()
            await message.answer(t["process_killed"].format(pid=pid))

        await state.clear()