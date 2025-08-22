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
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
import wmi

from config import ALLOWED_USER_ID 

def register_antivirus_handlers(dp):
    confirm_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Запустить", callback_data="antivirus_confirm"),
            InlineKeyboardButton(text="Отмена", callback_data="antivirus_cancel")
        ]
    ])

    @dp.message(F.text.lower() == "антивирус")
    @dp.message(Command("antivirus"))
    async def cmd_start(message: types.Message):
        await message.answer(
            "При сканировании возможна детекция антивирусами, используйте на свой страх и риск.",
            reply_markup=confirm_kb
        )

    @dp.callback_query(lambda c: c.data in ["antivirus_confirm", "antivirus_cancel"])
    async def process_antivirus_callback(callback: CallbackQuery):
        user_id = callback.from_user.id
        if user_id != ALLOWED_USER_ID:
            await callback.answer("У вас нет доступа к этой функции.", show_alert=True)
            return

        if callback.data == "antivirus_confirm":
            c = wmi.WMI(namespace="root/SecurityCenter2")
            antivirus_products = c.AntiVirusProduct()
            if antivirus_products:
                for product in antivirus_products:
                    await callback.message.answer("Установленные антивирусные программы: " + product.displayName)
            else:
                await callback.message.answer("Антивирусные программы не обнаружены.")
            await callback.answer("Проверка завершена, root.")
        else:
            await callback.answer("Отменено пользователем.")
            await callback.message.answer("Проверка антивирусов отменена.")
