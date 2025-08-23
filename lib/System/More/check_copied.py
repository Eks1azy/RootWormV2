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
from lib.states import clipboard
from lib.texts import TEXTS, user_languages

import pyperclip

def register_check_copied(dp):
    @dp.message(F.text.lower() == "посмотреть буфер обмена")
    @dp.message(F.text.lower() == "view clipboard")
    @dp.message(Command("clipboard_content"))
    async def conten(message: types.Message):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id == ALLOWED_USER_ID:
            clipboard_content = pyperclip.paste()
            await message.answer(f"{TEXTS[lang]['clipboard_content']}:\n{clipboard_content}")
        else:
            await message.answer(TEXTS[lang]['access_denied'])

    @dp.message(F.text.lower() == "изменить буфер обмена")
    @dp.message(F.text.lower() == "change clipboard")
    async def new_Clipboard(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['clipboard_ask_new'])
            await state.set_state(clipboard.waiting_for_newClipboard)
        else:
            await message.answer(TEXTS[lang]['access_denied'])

    @dp.message(clipboard.waiting_for_newClipboard)
    async def new_Clipboard_wait(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id == ALLOWED_USER_ID:
            new_text = message.text
            pyperclip.copy(new_text)
            await message.answer(TEXTS[lang]['clipboard_success'])
            await state.clear()
        else:
            await message.answer(TEXTS[lang]['access_denied'])