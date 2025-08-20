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
from aiogram.types import BufferedInputFile
from aiogram.filters import Command
from io import BytesIO
import pyautogui
from lib.texts import TEXTS, user_languages

from config import ALLOWED_USER_ID
 
def register_screenshot_handlers(dp):
    @dp.message(F.text.in_({"Скриншот", "Screenshot"}))
    @dp.message(Command("screenshot"))
    async def send_photo(message: types.Message):
        user_id = message.from_user.id

        # Определяем язык по кнопке или по словарю
        if message.text.lower() == "скриншот":
            lang = 'ru'
        else:
            lang = user_languages.get(user_id, 'en')

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang].get("access_denied", "You do not have access to this bot."))
            return

        await message.answer(TEXTS[lang].get("screenshot_start", "Taking screenshot now, root..."))

        try:
            screenshot = pyautogui.screenshot()
            buffer = BytesIO()
            screenshot.save(buffer, format='PNG')
            buffer.seek(0)

            photo = BufferedInputFile(buffer.read(), filename="screenshot.png")
            await message.answer_photo(photo)

        except Exception as e:
            await message.answer(TEXTS[lang].get("screenshot_error", f"Error sending screenshot: {e}"))