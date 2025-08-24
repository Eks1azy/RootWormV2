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
from aiogram.fsm.context import FSMContext
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from config import ALLOWED_USER_ID
from lib.texts import TEXTS, user_languages


def register_mute_handlers(dp):
    @dp.message(F.text.lower() == "выключить звук", "Mute sound")
    @dp.message(Command("mute_sound"))
    async def mute_sound_handler(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')
        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['no_access'])
            return

        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            volume.SetMute(1, None)  # 1 – выключить звук
            await message.answer(TEXTS[lang]['volune muted'])
        except Exception as e:
            await message.answer(f"Error: {e}")