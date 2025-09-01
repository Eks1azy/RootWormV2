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



import os
import cv2
import time
from aiogram import types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
from lib.states import WebTime

from config import ALLOWED_USER_ID, directory
from lib.text.texts import TEXTS, user_languages


def register_webcam_record_handlers(dp):
    @dp.message((F.text.lower() == "запись с веб камеры") | (F.text.lower() == "webcam record"))
    @dp.message(Command("web_record"))
    async def web_record(message: types.Message, state: FSMContext):
        await state.clear()
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]["ask_webcam_duration"])
            await state.set_state(WebTime.waiting_for_time)
        else:
            await message.answer(TEXTS[lang]["access_denied"])

    @dp.message(WebTime.waiting_for_time)
    async def start_recording(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]["access_denied"])
            return

        file_path = os.path.join(directory, 'webcam_video.mp4')

        try:
            try:
                recording_time = int(message.text)
                if recording_time <= 0:
                    raise ValueError
            except ValueError:
                await message.answer(TEXTS[lang]["invalid_duration"])
                return

            await message.answer(TEXTS[lang]["recording_started"])

            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                await message.answer(TEXTS[lang]["camera_busy"])
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
            await message.answer_video(file_to_send, caption=TEXTS[lang]["video_ready"])

        except Exception as e:
            await message.answer(f"{TEXTS[lang]['video_error']} {e}")

        finally:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except Exception as e:
                    await message.answer(f"{TEXTS[lang]['file_delete_error']} {file_path}: {e}")
            await state.clear()
