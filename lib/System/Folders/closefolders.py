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

def register_minimize_all_windows_handlers(dp):
    @dp.message(F.text.lower() == "свернуть все окна")
    @dp.message(Command("minimize_all_windows"))
    async def minimize_all_windows(message: types.Message):
        if message.from_user.id == ALLOWED_USER_ID:
            windows = gw.getAllWindows()
            for window in windows:
                if not window.isMinimized:
                    window.minimize()
            await message.answer("Окна были успешно свёрнуты")
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")