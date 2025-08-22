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



import os
from aiogram.filters import Command
from config import ALLOWED_USER_ID

def register_reboot_handlers(dp):
    @dp.message(lambda message: message.text and message.text.lower() == "перезагрузить пк")
    @dp.message(Command("restart_pc"))
    async def start_decipher(message):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer("ОК,перезагружаю ПК.")
            os.system('shutdown /r /t 1')
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")