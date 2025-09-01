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
from aiogram.fsm.context import FSMContext
from lib.Access.Audio.recordmic import start_audio_recording
from aiogram.fsm.state import State, StatesGroup
from lib.states import microfonetime

from lib.text.texts import TEXTS, user_languages
from config import ALLOWED_USER_ID, directory


def register_audio_handlers(dp):
    @dp.message((F.text.lower() == "запись аудио") | (F.text.lower() == "audio record"))
    @dp.message(Command("audio_record"))
    async def audio_record(message: types.Message, state: FSMContext):
        lang = user_languages.get(message.from_user.id, 'en')
        texts = TEXTS[lang]
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer(texts['ask_duration'])
            await state.set_state(microfonetime.waiting_for_microtime)
        else:
            await message.answer(texts['no_access'])

    @dp.message(microfonetime.waiting_for_microtime)
    async def process_audio_time_input(message: types.Message, state: FSMContext):
        lang = user_languages.get(message.from_user.id, 'en')
        texts = TEXTS[lang]

        if message.from_user.id == ALLOWED_USER_ID:
            try:
                recording_time = int(message.text)
                await start_audio_recording(message, state, recording_time)
            except ValueError:
                await message.answer(texts['invalid'])
                await state.clear()
        else:
            await message.answer(texts['no_access'])


# from config import ALLOWED_USER_ID, directory
# from aiogram.types import FSInputFile
# import wave
# import pyaudio
# import os
# from lib.texts import TEXTS, user_languages



# async def start_audio_recording(message, state, recording_time: int):
#     user_id = message.from_user.id
#     lang = user_languages.get(user_id, 'en') 

#     if user_id != ALLOWED_USER_ID:
#         await message.answer(TEXTS[lang].get("access_denied", "You do not have access to this bot."))
#         return

#     FORMAT = pyaudio.paInt16
#     CHANNELS = 1
#     RATE = 44100
#     CHUNK = 1024
#     OUTPUT_FILENAME = "output.wav"
#     save_audio = os.path.join(directory, OUTPUT_FILENAME)

#     audio = pyaudio.PyAudio()
#     stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

#     await message.answer(TEXTS[lang].get("recording_started", "Recording started..."))

#     frames = []
#     for _ in range(0, int(RATE / CHUNK * recording_time)):
#         data = stream.read(CHUNK)
#         frames.append(data)

#     await message.answer(TEXTS[lang].get("recording_finished", "Recording finished."))

#     stream.stop_stream()
#     stream.close()
#     audio.terminate()

#     wf = wave.open(save_audio, 'wb')
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(audio.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))
#     wf.close()

#     try:
#         file_to_send = FSInputFile(save_audio)
#         await message.answer_document(document=file_to_send, caption=TEXTS[lang].get("audio_ready", "Here is the audio recording, root!"))
#         os.remove(save_audio)
#         await state.clear()
#     except Exception as e:
#         await message.answer(TEXTS[lang].get("file_send_error", f"Error sending file: {e}"))
