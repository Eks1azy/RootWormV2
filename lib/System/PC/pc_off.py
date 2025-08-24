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
from lib.texts import TEXTS, user_languages


def register_shutdown_handlers(dp):
    @dp.message(lambda message: message.text and message.text.lower() in ["выключить пк", "shutdown pc"])
    @dp.message(Command("shutdown_pc"))
    async def shutdown_pc(message: types.Message):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['access_denied'])
            return

        await message.answer(TEXTS[lang]['shutdown_start'])
        os.system("shutdown /s /t 1")