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
import time
from aiogram import types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
from config import ALLOWED_USER_ID, directory
from lib.states import WebTime
from lib.texts import TEXTS, user_languages


def register_webcam_record_handlers(dp):
    @dp.message(F.text.lower().in_({"запись с веб камеры", "webcam record"}))
    @dp.message(Command("web_record"))
    async def web_record(message: types.Message, state: FSMContext):
        await state.clear()
        user_id = message.from_user.id

        lang = 'ru' if message.text.lower() == "запись с веб камеры" else user_languages.get(user_id, 'en')
        texts = TEXTS[lang]

        if user_id == ALLOWED_USER_ID:
            await message.answer(texts["ask_webcam_duration"])
            await state.set_state(WebTime.waiting_for_time)
        else:
            await message.answer(texts["access_denied"])

    @dp.message(WebTime.waiting_for_time)
    async def start_recording(message: types.Message, state: FSMContext):
        user_id = message.from_user.id

        # Язык определяется по последней известной команде (можно позже сохранить в state, если хочешь)
        lang = user_languages.get(user_id, 'en')
        texts = TEXTS[lang]

        if user_id != ALLOWED_USER_ID:
            await message.answer(texts["access_denied"])
            return

        file_path = os.path.join(directory, 'webcam_video.mp4')

        try:
            try:
                recording_time = int(message.text)
                if recording_time <= 0:
                    raise ValueError
            except ValueError:
                await message.answer(texts["invalid_duration"])
                return

            await message.answer(texts["recording_started"])

            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                await message.answer(texts["camera_busy"])
                return

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(file_path, fourcc, 20.0, (640, 480))

            start_time = time.time()
            while int(time.time() - start_time) < recording_time:
                ret, frame = cap.read()
                if ret:
                    out.write(frame)
                else:
                    break

            cap.release()
            out.release()

            file_to_send = FSInputFile(file_path)
            await message.answer_video(file_to_send, caption=texts["video_ready"])

        except Exception as e:
            await message.answer(f"{texts['video_error']} {e}")

        finally:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except Exception as e:
                    await message.answer(f"{texts['file_delete_error']} {file_path}: {e}")
            await state.clear()