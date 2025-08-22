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



import asyncio
import platform
import psutil
import GPUtil
import getpass
import socket
import aiohttp
from aiogram import types
from aiogram.filters import Command
from config import ALLOWED_USER_ID

def register_pc_data(dp):
    @dp.message(lambda message: message.text and message.text.lower() == "данные пк")
    @dp.message(Command("pc_data"))
    async def handle_message(message: types.Message):
        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")
            return

        try:

            try:
                cpu_info = {
                    'brand_raw': 'Неизвестно',
                    'arch': platform.architecture()[0],
                    'cores': psutil.cpu_count(logical=False),
                    'logical_cores': psutil.cpu_count(logical=True)
                }
            except Exception as e:
                await message.answer(f"Ошибка при сборе данных о процессоре: {e}")
                return

            try:
                gpus = GPUtil.getGPUs()
                if gpus:
                    gpu_info = f"Модель: {gpus[0].name}, Память: {gpus[0].memoryTotal} GB"
                else:
                    gpu_info = "Видеокарта не обнаружена"
            except Exception as e:
                gpu_info = f"Ошибка при сборе данных о видеокарте: {e}"


            system_info = platform.uname()
            user_name = getpass.getuser()

            async def fetch_public_ip():
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get('https://api.ipify.org?format=json', timeout=5) as response:
                            data = await response.json()
                            return data['ip']
                except asyncio.TimeoutError:
                    return "Превышено время ожидания для IP-адреса"
                except Exception as e:
                    return f"Ошибка при получении IP: {e}"

            async def fetch_ip_info():
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get("http://ip-api.com/json/", timeout=5) as response:
                            return await response.json()
                except asyncio.TimeoutError:
                    return {"error": "Превышено время ожидания для IP-информации"}
                except Exception as e:
                    return {"error": str(e)}

            public_ip, ip_info = await asyncio.gather(fetch_public_ip(), fetch_ip_info())

            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)

            report = f"""
            Архитектура процессора: {cpu_info['arch']}
            Количество ядер процессора: {cpu_info['cores']}
            Логическое количество ядер: {cpu_info['logical_cores']}
            Видеокарта: {gpu_info}
            Общая память ОЗУ: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB
            Система: {system_info.system} {system_info.release}
            Имя пользователя: {user_name}
            Имя ПК: {hostname}
            Публичный IP-адрес: {public_ip}
            Локальный IP-адрес: {local_ip}
            Данные локации и IP: {ip_info}
            """

            await message.answer(report)

        except Exception as e:
            await message.answer(f"Произошла ошибка при сборе данных: {e}")