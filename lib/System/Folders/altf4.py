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
import pyautogui
from config import ALLOWED_USER_ID


def register_alt_f4_handlers(dp):
    @dp.message(F.text.lower() == "alt + f4")
    @dp.message(Command("alt_f4"))
    async def alt_f4(message: types.Message):
        if message.from_user.id == ALLOWED_USER_ID:
            pyautogui.hotkey("alt", "f4")
            await message.answer("Окно было успешно закрыто ✅")
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")