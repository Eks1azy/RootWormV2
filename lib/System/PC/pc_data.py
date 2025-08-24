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
from lib.texts import TEXTS, user_languages

def register_pc_data(dp):
    @dp.message(lambda message: message.text and message.text.lower() in ["данные пк", "pc info"])
    @dp.message(Command("pc_data"))
    async def handle_message(message: types.Message):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]['access_denied'])
            return

        await message.answer(TEXTS[lang]['pc_data_start'])

        try:
            # 1. Получаем информацию о процессоре
            await message.answer(TEXTS[lang]['pc_data_cpu'])
            try:
                cpu_info = {
                    'brand_raw': 'Unknown' if lang == 'en' else 'Неизвестно',
                    'arch': platform.architecture()[0],
                    'cores': psutil.cpu_count(logical=False),
                    'logical_cores': psutil.cpu_count(logical=True)
                }
            except Exception as e:
                await message.answer(TEXTS[lang]['pc_data_cpu_error'].format(error=e))
                return
            await message.answer(TEXTS[lang]['pc_data_cpu_done'])

            # 2. Видеокарта
            await message.answer(TEXTS[lang]['pc_data_gpu'])
            try:
                gpus = GPUtil.getGPUs()
                if gpus:
                    gpu_info = f"Model: {gpus[0].name}, Memory: {gpus[0].memoryTotal} GB" if lang == 'en' else f"Модель: {gpus[0].name}, Память: {gpus[0].memoryTotal} GB"
                else:
                    gpu_info = TEXTS[lang]['pc_data_gpu_not_found']
            except Exception as e:
                gpu_info = TEXTS[lang]['pc_data_gpu_error'].format(error=e)
            await message.answer(TEXTS[lang]['pc_data_gpu_done'])

            # 3. Системная информация
            await message.answer(TEXTS[lang]['pc_data_system'])
            system_info = platform.uname()
            user_name = getpass.getuser()
            await message.answer(TEXTS[lang]['pc_data_system_done'])

            # 4. IP и сеть
            await message.answer(TEXTS[lang]['pc_data_network'])

            async def fetch_public_ip():
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get('https://api.ipify.org?format=json', timeout=5) as response:
                            data = await response.json()
                            return data['ip']
                except asyncio.TimeoutError:
                    return TEXTS[lang]['pc_data_ip_timeout']
                except Exception as e:
                    return TEXTS[lang]['pc_data_ip_error'].format(error=e)

            async def fetch_ip_info():
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get("http://ip-api.com/json/", timeout=5) as response:
                            return await response.json()
                except asyncio.TimeoutError:
                    return {"error": TEXTS[lang]['pc_data_ip_timeout']}
                except Exception as e:
                    return {"error": str(e)}

            public_ip, ip_info = await asyncio.gather(fetch_public_ip(), fetch_ip_info())
            await message.answer(TEXTS[lang]['pc_data_network_done'])

            # 5. Локальный IP и хост
            await message.answer(TEXTS[lang]['pc_data_local'])
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            await message.answer(TEXTS[lang]['pc_data_local_done'])

            # Формируем отчет
            report = TEXTS[lang]['pc_data_report'].format(
                cpu_arch=cpu_info['arch'],
                cpu_cores=cpu_info['cores'],
                logical_cores=cpu_info['logical_cores'],
                gpu_info=gpu_info,
                ram=psutil.virtual_memory().total / (1024 ** 3),
                system=f"{system_info.system} {system_info.release}",
                user=user_name,
                hostname=hostname,
                public_ip=public_ip,
                local_ip=local_ip,
                ip_info=ip_info
            )

            await message.answer(TEXTS[lang]['pc_data_report_sending'])
            await message.answer(report)

        except Exception as e:
            await message.answer(TEXTS[lang]['error_occurred'].format(error=e))