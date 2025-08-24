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
from aiogram.filters import Command
from aiogram import types
from config import ALLOWED_USER_ID
from lib.texts import TEXTS, user_languages

def register_reboot_handlers(dp):
    @dp.message(lambda message: message.text and message.text.lower() in ["перезагрузить пк", "reboot pc"])
    @dp.message(Command("restart_pc"))
    async def restart_pc(message: types.Message):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['access_denied'])
            return

        await message.answer(TEXTS[lang]['reboot_start'])
        os.system('shutdown /r /t 1')