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
from config import ALLOWED_USER_ID
import pygetwindow as gw
from lib.texts import TEXTS, user_languages

def register_minimize_all_windows_handlers(dp):
    @dp.message(F.text.lower().in_({"свернуть все окна", "minimize all windows"}))
    @dp.message(Command("minimize_all_windows"))
    async def minimize_all_windows(message: types.Message):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            windows = gw.getAllWindows()
            for window in windows:
                if not window.isMinimized:
                    window.minimize()
            await message.answer(TEXTS[lang]['minimize_windows_success'])
        else:
            await message.answer(TEXTS[lang]['no_access'])