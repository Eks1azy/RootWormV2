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
from lib.texts import TEXTS, user_languages

def register_discrypt(dp):
    @dp.message(F.text.lower().in_(["расшифровать файл", "decrypt file"]))
    @dp.message(Command("decipher_file"))
    async def start_decipher(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['ask_enc_path'])
            await state.set_state(Decipher.waiting_d_enc)
        else:
            await message.answer(TEXTS[lang]['no_access'])

    @dp.message(Decipher.waiting_d_enc)
    async def process_file_path(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
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

                    def decrypt_file(encrypted_file_path: str, password: str):
                        try:
                            with open(encrypted_file_path, 'rb') as f:
                                salt = f.read(16)
                                iv = f.read(16)
                                encrypted_data = f.read()

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
                        await message.answer(TEXTS[lang]['decryption_success'].format(
                            enc=encrypted_file_path, dec=new_file_path))

                        try:
                            os.remove(encrypted_file_path)
                            try:
                                os.rename(decrypted_file_path, new_file_path)
                            except FileNotFoundError:
                                await message.answer(TEXTS[lang]['rename_error_not_found'].format(path=decrypted_file_path))
                            except PermissionError:
                                await message.answer(TEXTS[lang]['rename_error_permission'].format(path=decrypted_file_path))
                            except Exception as e:
                                await message.answer(TEXTS[lang]['rename_error_general'].format(error=e))
                        except Exception as e:
                            logger.error(f"Ошибка при удалении файла {encrypted_file_path}: {e}")

                    elif decrypted_file_path is None:
                        await message.answer(TEXTS[lang]['decryption_error'].format(path=encrypted_file_path))
                else:
                    await message.answer(TEXTS[lang]['file_not_found'].format(path=encrypted_file_path))
            except Exception as e:
                logger.error(f"Ошибка при обработке пути файла {encrypted_file_path}: {e}")
                await message.answer(TEXTS[lang]['general_error'])
            finally:
                await state.clear()
        else:
            await message.answer(TEXTS[lang]['no_access'])