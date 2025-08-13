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
import psutil

from config import ALLOWED_USER_ID, MAX_MESSAGE_LENGTH

def register_full_processes_handlers(dp):
    @dp.message(F.text.lower() == "полный отчет по процесам")
    @dp.message(Command("fullprocesses"))
    async def cmd_start(message: types.Message):
        if message.from_user.id == ALLOWED_USER_ID:
            process_info_list = []

            for process in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info']):
                process_info = (
                    f"PID: {process.info['pid']}, Name: {process.info['name']}, "
                    f"User: {process.info['username']}, CPU: {process.info['cpu_percent']}%, "
                    f"Memory: {process.info['memory_info'].rss / (1024 * 1024):.2f} MB"
                )
                process_info_list.append(process_info)

            all_processes_info = "\n".join(process_info_list)

            # Разбиваем сообщение на части, если оно превышает лимит
            for i in range(0, len(all_processes_info), MAX_MESSAGE_LENGTH):
                await message.answer(all_processes_info[i:i + MAX_MESSAGE_LENGTH])
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
