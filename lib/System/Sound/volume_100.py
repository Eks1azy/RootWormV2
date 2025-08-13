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

def register_volume_100(dp):
    @dp.message(F.text.lower() == "звук на 100%")
    @dp.message(Command("set_volume_100"))
    async def open_url(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:

            def set_volume_to_100():
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))

                # Установка громкости на 100% (1.0 означает 100%)
                volume.SetMasterVolumeLevelScalar(1.0, None)

            set_volume_to_100()
            await message.answer("Громкость была установлена на 100%")
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
