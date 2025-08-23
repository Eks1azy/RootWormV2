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
from lib.texts import TEXTS, user_languages

import psutil

def register_close_dp(dp):
    @dp.message(F.text.lower() == "закрыть диспетчер задач")
    @dp.message(F.text.lower() == "close task manager")
    @dp.message(Command("close_task_manager"))
    async def open_url(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id == ALLOWED_USER_ID:
            # Проходим по всем процессам и ищем "Taskmgr.exe"
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == 'Taskmgr.exe':
                    psutil.Process(proc.info['pid']).terminate()
                    await message.answer(TEXTS[lang]['task_manager_closed'])
                    break
            else:
                await message.answer(TEXTS[lang]['task_manager_not_running'])
        else:
            await message.answer(TEXTS[lang]['access_denied'])