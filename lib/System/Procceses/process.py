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
from config import ALLOWED_USER_ID, MAX_MESSAGE_LENGTH
from lib.texts import TEXTS, user_languages
import psutil


def register_processes_handlers(dp):
    @dp.message(F.text.lower() == "процесы")
    @dp.message(F.text.lower() == "processes")
    @dp.message(Command("processes"))
    async def show_processes(message: types.Message):
        lang = user_languages.get(message.from_user.id, 'ru')
        t = TEXTS[lang]

        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer(t["no_access"])
            return

        process_info_list = []

        for process in psutil.process_iter(['pid', 'name']):
            try:
                process_info = f"PID: {process.info['pid']}, {process.info['name']}"
                process_info_list.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        all_processes_info = f"{t['short_process_report_title']}\n\n" + "\n".join(process_info_list)

        for i in range(0, len(all_processes_info), MAX_MESSAGE_LENGTH):
            await message.answer(all_processes_info[i:i + MAX_MESSAGE_LENGTH])