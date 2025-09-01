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



from aiogram import types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile

import datetime
import os
import shutil
import sqlite3

from config import ALLOWED_USER_ID, directory
from lib.text.texts import TEXTS, user_languages

def register_chrome_history_handlers(dp):
    @dp.message((F.text.lower() == "история хрома") | (F.text.lower() == "chrome history"))
    @dp.message(Command("chrome_history"))
    async def cmd_start(message: types.Message):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['access_denied'])
            return

        await message.answer(TEXTS[lang]['chrome_history_start'])

        def get_chrome_history():
            history_path = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\Default\History')

            if not os.path.exists(history_path):
                return False, TEXTS[lang]['chrome_history_not_found']

            temp_history_path = 'temp_history'
            shutil.copy2(history_path, temp_history_path)

            conn = sqlite3.connect(temp_history_path)
            cursor = conn.cursor()

            query = """
            SELECT urls.url, urls.title, urls.last_visit_time
            FROM urls
            ORDER BY last_visit_time DESC
            """
            cursor.execute(query)

            rows = cursor.fetchall()

            text_to_save = ""
            for row in rows:
                url = row[0]
                title = row[1]
                last_visit_time = row[2]

                try:
                    if last_visit_time > 0:
                        last_visit_time = last_visit_time / 1000000 - 11644473600
                        last_visit_time = datetime.datetime.fromtimestamp(last_visit_time).strftime('%Y-%m-%d %H:%M:%S')
                    else:
                        last_visit_time = TEXTS[lang]['invalid_time']
                except (OSError, ValueError) as e:
                    last_visit_time = f"{TEXTS[lang]['error_time']}: {str(e)}"

                text_to_save += f"URL: {url}\nTitle: {title}\nLast Visit: {last_visit_time}\n\n"

            file_path = os.path.join(directory, TEXTS[lang]['chrome_history_filename'])

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text_to_save)

            conn.close()
            os.remove(temp_history_path)

            return True, file_path

        success, result = get_chrome_history()

        if not success:
            await message.answer(result)
            return

        file_path = result
        try:
            file_to_send = FSInputFile(file_path)
            await message.answer_document(document=file_to_send, caption=TEXTS[lang]['chrome_history_caption'])
        except Exception as e:
            await message.answer(f"{TEXTS[lang]['chrome_history_send_error']}: {e}")
        os.remove(file_path)
