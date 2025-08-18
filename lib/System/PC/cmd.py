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
from lib.states import CommandShell

import subprocess


def register_cmd_comand(dp):
    @dp.message(F.text.lower() == "командная строка")
    @dp.message(Command("cmd"))
    async def start_cmd(message: types.Message, state: FSMContext):
        if message.from_user.id == ALLOWED_USER_ID:
            await message.answer("Командная строка активна. Введите команду:\n\nЧтобы выйти — напиши `exit`.")
            await state.set_state(CommandShell.waiting_command)
        else:
            await message.answer("У вас нет доступа к этому боту.")

    @dp.message(CommandShell.waiting_command)
    async def process_command(message: types.Message, state: FSMContext):
        if message.from_user.id != ALLOWED_USER_ID:
            await message.answer("У вас нет доступа к этому боту.")
            return

        cmd = message.text.strip()

        if cmd.lower() in ["exit", "выход", "quit"]:
            await state.clear()
            await message.answer("Вы вышли из режима командной строки.")
            return

        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='cp866', timeout=15)
            output = result.stdout or result.stderr or "Команда выполнена, но вывода нет."
        except Exception as e:
            output = f"Ошибка выполнения: {e}"

        if len(output) > 4000:
            output = output[:4000] + "\n\nВывод обрезан..."

        await message.answer(f"Command:\n`{cmd}`\nResult:\n```\n{output}\n```", parse_mode="Markdown")
