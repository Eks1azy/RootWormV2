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
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from config import ALLOWED_USER_ID, bot, MAX_ATTEMPTS
from lib.states import DirectoryStateSaveFiles
from aiogram.types import ContentType

import os 

def register_load_file(dp):
    @dp.message(F.text.lower() == "загрузить файл")
    @dp.message(Command("upload_file"))
    async def handle_text_message(message: types.Message, state: FSMContext):
        if message.text.lower() == "загрузить файл":
            if message.from_user.id == ALLOWED_USER_ID:
                await message.answer(
                    "Укажите путь, куда необходимо загрузить файл, пример:\n C:/Users/Public"
                )
                await state.set_state(DirectoryStateSaveFiles.waiting_for_directory_saveFiles)  # Переход в состояние ожидания пути файла
                await state.update_data(attempts=0)  # Инициализация счетчика попыток

            else:
                await message.answer("К сожалению, у вас нет доступа к этому боту.")

    # Обработчик для ввода новой директории
    @dp.message(DirectoryStateSaveFiles.waiting_for_directory_saveFiles)
    async def set_new_directory(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            directoryForSaveFiles = message.text
            data = await state.get_data()
            attempts = data.get('attempts', 0)

            if not directoryForSaveFiles or not os.path.isdir(directoryForSaveFiles):
                attempts += 1
                if attempts >= MAX_ATTEMPTS:
                    await message.answer("Не удалось найти директорию. Повторите попытку, перезапустив процесс.")
                    await state.clear()  # Завершаем состояние

            else:
                await state.update_data(directoryForSaveFiles=directoryForSaveFiles, attempts=0)
                await message.answer(
                    f'Отправьте файл, который будет сохранен по этому пути:\n{directoryForSaveFiles}')
                await state.set_state(DirectoryStateSaveFiles.waiting_for_files)

        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    @dp.message(DirectoryStateSaveFiles.waiting_for_files, F.content_type.in_([ContentType.PHOTO, ContentType.DOCUMENT, ContentType.AUDIO]))
    async def handle_document_or_audio(message: types.Message, state: FSMContext):
        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
            return

        user_data = await state.get_data()
        directoryForSaveFiles = user_data.get('directoryForSaveFiles')

        if not directoryForSaveFiles or not os.path.isdir(directoryForSaveFiles):
            await message.reply("Необходимо сначала указать корректный путь для сохранения файла. \nПопробуйте снова, перезапустив команду.")
            await state.clear()
            return

        # Выбор файла (документ, фото, аудио)
        if message.document:
            document = message.document
            file_id = document.file_id
            file_name = document.file_name if document.file_name else "document.bin"
        elif message.photo:
            document = message.photo[-1]
            file_id = document.file_id
            file_name = "photo.jpg"
        elif message.audio:
            document = message.audio
            file_id = document.file_id
            file_name = document.file_name if document.file_name else "audio.mp3"
        else:
            await message.reply("В сообщении нет поддерживаемого файла.")
            return

        try:
            await message.reply("Принял, сохраняю...")
            file_info = await bot.get_file(file_id)
            file_path = file_info.file_path

            file = await bot.download_file(file_path)
            save_path = os.path.join(directoryForSaveFiles, file_name)

            with open(save_path, 'wb') as f:
                f.write(file.read())

            await message.reply(f"Файл '{file_name}' успешно сохранён в:\n{directoryForSaveFiles}")
            await state.clear()

        except Exception as e:
            await message.reply(f"Ошибка при сохранении файла: {e}")
            await state.clear()