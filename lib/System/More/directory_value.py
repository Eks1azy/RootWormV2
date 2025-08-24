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
from lib.states import current_directory
from lib.texts import TEXTS, user_languages

import os

def register_directory_value(dp):
    @dp.message(F.text == "Содержание директории")
    @dp.message(F.text == "Directory content")
    @dp.message(Command("show_directory_content"))
    async def show_directory_content(message: types.Message):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id == ALLOWED_USER_ID:
            global current_directory
            try:
                files_and_dirs = os.listdir(current_directory)
                content = []
                for item in files_and_dirs:
                    full_path = os.path.join(current_directory, item)
                    if os.path.isfile(full_path):
                        size = os.path.getsize(full_path)
                        content.append(f"{item}  -  {size / (1024 * 1024):.2f} MB")
                    else:
                        content.append(f"{item}")
                content_text = "\n".join(content) if content else TEXTS[lang]['folder_empty']
            except Exception as e:
                content_text = f"{TEXTS[lang]['error']}: {str(e)}"

            await message.answer(f"{TEXTS[lang]['directory_content']} '{current_directory}':`\n{content_text}`", parse_mode='MarkdownV2')
        else:
            await message.answer(TEXTS[lang]['access_denied'])