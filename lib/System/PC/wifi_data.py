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
from aiogram.fsm.context import FSMContext
from config import ALLOWED_USER_ID
from lib.texts import TEXTS, user_languages

import subprocess
import psutil
import socket
import requests

def register_wifi_data(dp):
    @dp.message(lambda message: message.text and message.text.lower() in ["диагностика сети", "network diagnostics"])
    @dp.message(Command("network_diagnostics"))
    async def handle_network_diagnostics(message: types.Message):
        user_id = message.from_user.id
        lang = user_languages.get(user_id, 'en')

        if user_id != ALLOWED_USER_ID:
            await message.answer(TEXTS[lang]["no_access"])
            return

        await message.answer(TEXTS[lang]["network_start"])

        async def ping(host):
            try:
                result = subprocess.run(["ping", "-n", "4", host], capture_output=True, text=True)
                return result.stdout
            except Exception as e:
                return f"{TEXTS[lang]['ping_error']}: {e}"

        async def traceroute(host):
            try:
                result = subprocess.run(["tracert", host], capture_output=True, text=True)
                return result.stdout
            except Exception as e:
                return f"{TEXTS[lang]['traceroute_error']}: {e}"

        async def scan_ports(host, ports):
            open_ports = []
            for port in ports:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    if sock.connect_ex((host, port)) == 0:
                        open_ports.append(port)
                    sock.close()
                except Exception as e:
                    return f"{TEXTS[lang]['port_scan_error']}: {e}"
            return open_ports

        async def get_network_info():
            try:
                info = {}
                for iface, addrs in psutil.net_if_addrs().items():
                    info[iface] = {addr.family.name: addr.address for addr in addrs}
                return info
            except Exception as e:
                return f"{TEXTS[lang]['net_info_error']}: {e}"

        async def resolve_dns(host):
            try:
                ip = socket.gethostbyname(host)
                return f"{TEXTS[lang]['dns_result']} {host}: {ip}"
            except Exception as e:
                return f"{TEXTS[lang]['dns_error']}: {e}"

        async def check_website(url):
            try:
                response = requests.get(url)
                return f"{TEXTS[lang]['website_status']} {url}: {response.status_code} ({response.reason})"
            except Exception as e:
                return f"{TEXTS[lang]['website_error']}: {e}"

        async def get_external_ip():
            try:
                response = requests.get('https://api.ipify.org?format=json')
                return f"{TEXTS[lang]['external_ip']}: {response.json().get('ip')}"
            except Exception as e:
                return f"{TEXTS[lang]['external_ip_error']}: {e}"

        async def network_traffic():
            try:
                net_info = psutil.net_io_counters()
                return (f"{TEXTS[lang]['traffic_received']}: {net_info.bytes_recv / 1_000_000:.2f} MB\n"
                        f"{TEXTS[lang]['traffic_sent']}: {net_info.bytes_sent / 1_000_000:.2f} MB")
            except Exception as e:
                return f"{TEXTS[lang]['traffic_error']}: {e}"

        async def get_mtu(interface):
            try:
                mtu = psutil.net_if_stats()[interface].mtu
                return f"{TEXTS[lang]['mtu']} {interface}: {mtu}"
            except Exception as e:
                return f"{TEXTS[lang]['mtu_error']}: {e}"

        async def generate_report():
            report = [TEXTS[lang]["network_report"] + "\n"]

            try:
                report.append(TEXTS[lang]["ping_results"] + "\n")
                report.append(await ping("google.com") + "\n")

                report.append(TEXTS[lang]["traceroute_results"] + "\n")
                report.append(await traceroute("google.com") + "\n")

                report.append(TEXTS[lang]["port_scan_results"] + "\n")
                open_ports = await scan_ports("localhost", [22, 80, 443, 8080])
                report.append(f"{TEXTS[lang]['open_ports']}: {open_ports}\n")

                report.append(TEXTS[lang]["network_info"] + "\n")
                network_info = await get_network_info()
                if isinstance(network_info, dict):
                    for iface, addresses in network_info.items():
                        report.append(f"{iface}: {addresses}\n")
                else:
                    report.append(network_info + "\n")

                report.append(TEXTS[lang]["additional_info"] + "\n")
                report.append(await resolve_dns("google.com") + "\n")
                report.append(await check_website("https://google.com") + "\n")
                report.append(await get_external_ip() + "\n")
                report.append(await network_traffic() + "\n")
                for iface in psutil.net_if_stats():
                    report.append(await get_mtu(iface) + "\n")
            except Exception as e:
                report.append(f"{TEXTS[lang]['report_error']}: {e}\n")

            await message.answer("".join(report))

        await generate_report()