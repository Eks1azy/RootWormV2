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
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from aiogram.fsm.context import FSMContext
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from config import ALLOWED_USER_ID
from lib.states import Encrypt
from lib.states import logger

import os


def register_encrypt_handlers(dp):
    dp.message(F.text.lower() == "зашифровать файл")
    @dp.message(Command("encrypt_file"))
    async def start_encryption(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer("Укажите путь и расширение файла, пример:\n C:/Users/Public/Название_файла.txt")
            await state.set_state(Encrypt.waiting_d)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    @dp.message(Encrypt.waiting_d)
    async def process_file_path(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            file_path = message.text

            try:
                # Проверяем, существует ли файл
                if os.path.exists(file_path):
                    # Функция для генерации ключа на основе пароля
                    def generate_key(password: str, salt: bytes) -> bytes:
                        kdf = Scrypt(
                            salt=salt,
                            length=32,
                            n=2 ** 14,
                            r=8,
                            p=1,
                            backend=default_backend()
                        )
                        return kdf.derive(password.encode())

                    # Функция шифрования данных
                    def encrypt_file(file_path: str, password: str):
                        try:
                            salt = os.urandom(16)
                            key = generate_key(password, salt)

                            iv = os.urandom(16)
                            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
                            encryptor = cipher.encryptor()

                            with open(file_path, 'rb') as f:
                                file_data = f.read()

                            # Добавление padding, так как AES работает с блоками данных
                            padder = padding.PKCS7(128).padder()
                            padded_data = padder.update(file_data) + padder.finalize()

                            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

                            # Запись зашифрованных данных в новый файл
                            with open(file_path + '.enc', 'wb') as f:
                                f.write(salt + iv + encrypted_data)

                        except Exception as e:
                            logger.error(f"Ошибка при шифровании файла {file_path}: {e}")
                            return False
                        return True

                    password = 'kjesbfskjfbalga;ewgb/gebiwekwfnwgwawgeogk4egikaleikdrinlomgs;oegm'  # Пароль для шифрования
                    success = encrypt_file(file_path, password)

                    if success:
                        try:
                            # Удаляем исходный файл после шифрования
                            os.remove(file_path)
                        except Exception as e:
                            logger.error(f"Ошибка при удалении файла {file_path}: {e}")
                            await message.answer(f'Файл {file_path} успешно зашифрован, но произошла ошибка при удалении исходного файла.')

                        await message.answer(f'Файл {file_path} успешно зашифрован и сохранён как {file_path}.enc')
                    else:
                        await message.answer(f'Произошла ошибка при шифровании файла {file_path}. Процесс прекращён.')
                else:
                    await message.answer(f"Файл {file_path} не был найден. \nПожалуйста, проверьте правильность пути и имени файла, затем повторите попытку.")

            except Exception as e:
                logger.error(f"Ошибка при обработке пути файла {file_path}: {e}")
                await message.answer("Произошла ошибка. Попробуйте снова.")
            finally:
                # Завершаем состояние с помощью метода clear
                await state.clear()
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")