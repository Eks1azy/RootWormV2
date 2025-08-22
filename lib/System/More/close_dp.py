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

import psutil

def register_close_dp(dp):
    @dp.message(F.text.lower() == "закрыть диспетчер задач")
    @dp.message(Command("close_task_manager"))
    async def open_url(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == 'Taskmgr.exe':
                    psutil.Process(proc.info['pid']).terminate()
                    await message.answer("Task Manager закрыт, root.")
                    break
            else:
                await message.answer("Диспетчер задач не запущен, root.")

        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")