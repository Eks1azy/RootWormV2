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
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from aiogram.fsm.context import FSMContext
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from config import ALLOWED_USER_ID
from lib.states import Encrypt
from lib.states import logger
from lib.texts import TEXTS, user_languages

import os


def register_encrypt_handlers(dp):
    @dp.message(F.text.lower().in_(["зашифровать файл", "encrypt file"]))
    @dp.message(Command("encrypt_file"))
    async def start_encryption(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['ask_encrypt_path'])  # новый ключ
            await state.set_state(Encrypt.waiting_d)
        else:
            await message.answer(TEXTS[lang]['no_access'])

    @dp.message(Encrypt.waiting_d)
    async def process_file_path(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'ru')

        if user_id == ALLOWED_USER_ID:
            file_path = message.text

            try:
                if os.path.exists(file_path):
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

                    def encrypt_file(file_path: str, password: str):
                        try:
                            salt = os.urandom(16)
                            key = generate_key(password, salt)

                            iv = os.urandom(16)
                            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
                            encryptor = cipher.encryptor()

                            with open(file_path, 'rb') as f:
                                file_data = f.read()

                            padder = padding.PKCS7(128).padder()
                            padded_data = padder.update(file_data) + padder.finalize()

                            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

                            with open(file_path + '.enc', 'wb') as f:
                                f.write(salt + iv + encrypted_data)

                        except Exception as e:
                            logger.error(f"Ошибка при шифровании файла {file_path}: {e}")
                            return False
                        return True

                    password = 'kjesbfskjfbalga;ewgb/gebiwekwfnwgwawgeogk4egikaleikdrinlomgs;oegm'
                    success = encrypt_file(file_path, password)

                    if success:
                        try:
                            os.remove(file_path)
                        except Exception as e:
                            logger.error(f"Ошибка при удалении файла {file_path}: {e}")
                            await message.answer(TEXTS[lang]['encrypt_success_with_delete_error'].format(path=file_path))

                        await message.answer(TEXTS[lang]['encrypt_success'].format(path=file_path, enc_path=file_path + '.enc'))
                    else:
                        await message.answer(TEXTS[lang]['encrypt_error'].format(path=file_path))
                else:
                    await message.answer(TEXTS[lang]['file_not_found'].format(path=file_path))

            except Exception as e:
                logger.error(f"Ошибка при обработке пути файла {file_path}: {e}")
                await message.answer(TEXTS[lang]['general_error'])
            finally:
                await state.clear()
        else:
            await message.answer(TEXTS[lang]['no_access'])