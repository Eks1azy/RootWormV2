##  _________________________________________
##   |_______  authors: NoNamedExe  _______| 
##    \_\_\_|______  Oqwe4O  _______|\_\_\_\
##           \_\_\_\_\_\_\_\_\_\_\_\                    
##  ___________________________________________
##  |                                          /\
##  |  github:https://github.com/NoNamedExe   / /
##  |                                        / / 
##  |    if you will find some bugs or      / /
##  |                                      / /
##  |    have ideas for improvements,     / /
##  |                                    / /
##  |       please send it to me        / /
##  |__________________________________/ /
##  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/


from library import *
from config import ALLOWED_USER_ID

def register_check_copied(dp):
    @dp.message(F.text.lower() == "посмотреть буфер обмена")
    @dp.message(Command("clipboard_content"))
    async def conten(message: types.Message):
        if message.from_user.id == ALLOWED_USER_ID:
            clipboard_content = pyperclip.paste()

            await message.answer(f"Содержимое буфера обмена:\n{clipboard_content}")

        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    class clipboard(StatesGroup):
        waiting_for_newClipboard = State()
    @dp.message(F.text.lower() == "изменить буфер обмена")
    async def new_Clipboard(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer("Хорошо, отправь мне текст на который хочешь заменить буфер обмена")
            await state.set_state(clipboard.waiting_for_newClipboard)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    @dp.message(clipboard.waiting_for_newClipboard)
    async def new_Clipboard_wait(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            new_text = message.text

            # Помещаем текст в буфер обмена
            pyperclip.copy(new_text)

            await message.answer("Текст успешно помещен в буфер обмена!")
            await state.clear()
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
