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
from config import ALLOWED_USER_ID


def register_shutdown_handlers(dp):
    @dp.message(F.text.lower() == "выключить пк")
    @dp.message(Command("shutdown_pc"))
    async def shutdown_pc(message: types.Message):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer("ОК, выключаю ПК.")
            os.system("shutdown /s /t 1")
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")