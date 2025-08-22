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
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from config import ALLOWED_USER_ID

def set_mute(state: int):
    """state = 1 → выключить звук, state = 0 → включить"""
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(state, None)

def register_sound_handlers(dp):
    @dp.message(F.text.lower() == "выключить звук")
    @dp.message(Command("mute_sound"))
    async def mute_sound_handler(message: types.Message, state: FSMContext):
        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
            return

        try:
            set_mute(1)
            await message.answer("Звук отключен.")
        except Exception as e:
            await message.answer(f"Ошибка: {e}")

    @dp.message(F.text.lower() == "включить звук")
    @dp.message(Command("unmute_sound"))
    async def unmute_sound_handler(message: types.Message, state: FSMContext):
        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
            return

        try:
            set_mute(0)
            await message.answer("Звук включен.")
        except Exception as e:
            await message.answer(f"Ошибка: {e}")