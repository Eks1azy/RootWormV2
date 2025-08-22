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
from config import ALLOWED_USER_ID

import subprocess
import psutil
import socket
import requests

def register_wifi_data(dp):
    @dp.message(lambda message: message.text and message.text.lower() == "диагностика сети")
    @dp.message(Command("network_diagnostics"))
    async def handle_network_diagnostics(message: types.Message):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer("Собираем данные это может занять некоторое время.")
            async def ping(host):
                try:
                    result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
                    return result.stdout
                except Exception as e:
                    return f"Ошибка пинга: {e}"

            async def traceroute(host):
                try:
                    result = subprocess.run(["traceroute", host], capture_output=True, text=True)
                    return result.stdout
                except Exception as e:
                    return f"Ошибка трассировки: {e}"

            async def scan_ports(host, ports):
                open_ports = []
                for port in ports:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(1)
                        result = sock.connect_ex((host, port))
                        if result == 0:
                            open_ports.append(port)
                        sock.close()
                    except Exception as e:
                        return f"Ошибка сканирования портов: {e}"
                return open_ports

            async def get_network_info():
                try:
                    info = {}
                    for iface, addrs in psutil.net_if_addrs().items():
                        info[iface] = {addr.family.name: addr.address for addr in addrs}
                    return info
                except Exception as e:
                    return f"Ошибка получения информации о сети: {e}"

            async def resolve_dns(host):
                try:
                    ip = socket.gethostbyname(host)
                    return f"IP-адрес для {host}: {ip}"
                except Exception as e:
                    return f"Ошибка разрешения DNS: {e}"

            async def check_website(url):
                try:
                    response = requests.get(url)
                    return f"Статус сайта {url}: {response.status_code} ({response.reason})"
                except Exception as e:
                    return f"Ошибка доступа к сайту: {e}"

            async def get_external_ip():
                try:
                    response = requests.get('https://api.ipify.org?format=json')
                    return f"Внешний IP-адрес: {response.json().get('ip')}"
                except Exception as e:
                    return f"Ошибка получения внешнего IP: {e}"

            async def network_traffic():
                try:
                    net_info = psutil.net_io_counters()
                    return (f"Принято данных: {net_info.bytes_recv / 1_000_000:.2f} МБ\n"
                            f"Отправлено данных: {net_info.bytes_sent / 1_000_000:.2f} МБ")
                except Exception as e:
                    return f"Ошибка получения информации о трафике: {e}"

            async def get_mtu(interface):
                try:
                    mtu = psutil.net_if_stats()[interface].mtu
                    return f"MTU для интерфейса {interface}: {mtu}"
                except Exception as e:
                    return f"Ошибка получения MTU: {e}"

            async def generate_report():
                report = []
                report.append("Отчет о сети\n")

                try:
                    # Пинг
                    report.append("Результаты пинга:\n")
                    report.append(await ping("google.com") + "\n")

                    # Трассировка маршрута
                    report.append("Результаты трассировки маршрута:\n")
                    report.append(await traceroute("google.com") + "\n")

                    # Сканирование портов
                    report.append("Результаты сканирования портов:\n")
                    open_ports = await scan_ports("localhost", [22, 80, 443, 8080])
                    report.append(f"Открытые порты: {open_ports}\n")

                    # Информация о сети
                    report.append("Информация о сети:\n")
                    network_info = await get_network_info()
                    if isinstance(network_info, dict):
                        for iface, addresses in network_info.items():
                            report.append(f"{iface}: {addresses}\n")
                    else:
                        report.append(network_info + "\n")

                    # Дополнительная информация
                    report.append("Дополнительная информация:\n")
                    report.append(await resolve_dns("google.com") + "\n")
                    report.append(await check_website("https://google.com") + "\n")
                    report.append(await get_external_ip() + "\n")
                    report.append(await network_traffic() + "\n")
                    for iface in psutil.net_if_stats():
                        report.append(await get_mtu(iface) + "\n")

                except Exception as e:
                    report.append(f"Ошибка при создании отчета: {e}\n")

                # Вывод отчета
                await message.answer("".join(report))

            await generate_report()
        else:
            await message.answer("К сожалению, у вас нет доступа к этому боту.")