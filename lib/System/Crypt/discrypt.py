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


from lib.states import Decipher
from lib.states import logger
from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from config import ALLOWED_USER_ID
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
import time
from cryptography.hazmat.backends import default_backend

def register_discrypt(dp):
    @dp.message(F.text.lower() == "расшифровать файл")
    @dp.message(Command("decipher_file"))
    async def start_decipher(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer("Укажите путь и расширение файла и в конце укажите '.enc', пример:\n C:/Users/Public/Название_файла.txt.enc")
            await state.set_state(Decipher.waiting_d_enc)
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")

    @dp.message(Decipher.waiting_d_enc)
    async def process_file_path(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            encrypted_file_path = message.text

            try:
                if os.path.exists(encrypted_file_path):
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

                    # Функция расшифровки данных
                    def decrypt_file(encrypted_file_path: str, password: str):
                        try:
                            with open(encrypted_file_path, 'rb') as f:
                                # Считываем соль, IV и зашифрованные данные
                                salt = f.read(16)  # Первые 16 байт - это соль
                                iv = f.read(16)  # Следующие 16 байт - это IV
                                encrypted_data = f.read()  # Остальные данные - зашифрованные

                            key = generate_key(password, salt)

                            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
                            decryptor = cipher.decryptor()

                            decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

                            unpadder = padding.PKCS7(128).unpadder()
                            decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

                            decrypted_file_path = encrypted_file_path.replace('.enc', '.txt')
                            with open(decrypted_file_path, 'wb') as f:
                                f.write(decrypted_data)

                            return decrypted_file_path

                        except Exception as e:
                            logger.error(f"Ошибка при расшифровке файла {encrypted_file_path}: {e}")
                            return None

                    password = 'kjesbfskjfbalga;ewgb/gebiwekwfnwgwawgeogk4egikaleikdrinlomgs;oegm' 
                    decrypted_file_path = decrypt_file(encrypted_file_path, password)
                    new_file_path = os.path.splitext(decrypted_file_path)[0]

                    if decrypted_file_path and os.path.exists(decrypted_file_path):
                        await message.answer(f'Файл {encrypted_file_path} успешно расшифрован как {new_file_path}')

                        try:
                            os.remove(encrypted_file_path)
                            try:
                                os.rename(decrypted_file_path, new_file_path)
                            except FileNotFoundError:
                                await message.answer(f"Файл {decrypted_file_path} не найден")
                            except PermissionError:
                                await message.answer(f"Нет прав на изменение имени файла {decrypted_file_path}")
                            except Exception as e:
                                await message.answer(f"Произошла ошибка: {e}")

                        except Exception as e:
                            logger.error(f"Ошибка при удалении файла {encrypted_file_path}: {e}")

                    elif decrypted_file_path is None:
                        await message.answer(f'Произошла ошибка при расшифровке файла {encrypted_file_path}. Процесс прекращён.')
                else:
                    await message.answer(f"Файл {encrypted_file_path} не был найден. \nПожалуйста, проверьте правильность пути и имени файла, затем повторите попытку.")
            except Exception as e:
                logger.error(f"Ошибка при обработке пути файла {encrypted_file_path}: {e}")
                await message.answer("Произошла ошибка. Попробуйте снова.")
            finally:
                # Завершаем состояние с помощью метода clear
                await state.clear()
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
