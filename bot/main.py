import asyncio
import logging
import config


import keyboards

from contextlib import suppress
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest



logging.basicConfig(level=logging.INFO)


tarif = [
    ["Приватка:", "\nПриватка на 1 месяц - 200р\nПриватка на 3 месяца - 600р\nПриватка на БЕСКОЧНО - 800р\n\nДля оплты писать @HEALTyXA"],
    ["Фотки:", "\nФото 5шт - 50р\nФото 15шт - 150р\nФото 30шт - 300р\n\nДля оплты писать @HEALTyXA"],
    ["Заказные фотки:", "\nЗаказное фото от 100р (чем сложнее фото тем больше цена)\n\nДля оплты писать @HEALTyXA"],
    ["Реклма:", "\nПост в ТГК - 100р\nРассылка в боте - 300р\nПост в ТГК и рассылка в боте - 500р\n\nДля оплты писать @HEALTyXA"]
    
]

bot = Bot(token=config.TOKEN, parse_mode="HTML")
dp = Dispatcher()

# будущая база данных 


# /start and menu

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(f"<b>Приветик @{message.from_user.username}❤! Вот меню:</b>", reply_markup=keyboards.start_kb)

@dp.callback_query(keyboards.Pagination.filter(F.action.in_(["prev", "next"])))
async def pagination_handler(call: CallbackQuery, callback_data: keyboards.Pagination):
    page_num = int(callback_data.page)
    page = page_num - 1 if page_num > 0 else 0

    if callback_data.action == "next":
        page = page_num + 1 if page_num < (len(tarif) - 1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.edit_text(
            f"{tarif[page][0]} <b>{tarif[page][1]}</b>",
            reply_markup=keyboards.paginator(page)
        )
    await call.answer()


# ссылки и прочее

@dp.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == "ссылки":
        await message.answer("<b>Вот твои ссылкочки, котик🎈</b>", reply_markup=keyboards.links_kb)
    elif msg == "информация":
        await message.answer("<b>Это телеграмм бот создан для оповищений и оплаты моей приваточки с горячими фоточками))</b>\n<b>Купить приватку можно нажав на 'Тарифы' и Выбрать нужную услугу</b>")
    elif msg == "тарифы":
        await message.answer(f"{tarif[0][0]} <b>{tarif[0][1]}</b>", reply_markup=keyboards.paginator())
    elif msg == "спец.кнопки":
         await message.answer("<b>Вот твои спец.кнопочки, котик💗:</b>", reply_markup=keyboards.spec_kb)
    elif msg == "хотелки":
        await message. answer("<b>Хотелояки лизы тут! ⬇ </b>", reply_markup=keyboards.xotelki_kb)
    elif msg == "вернуться":
        await message.answer("<b>ты в главном меню котик💖</b>", reply_markup=keyboards.start_kb)
    elif msg == "игрулька":
        await message.answer("<b>Скоро добавим котик</b>",reply_markup=keyboards.start_kb)
    
    


# Обработчик текста
@dp.message()
async def echo(message: Message):
    await message.answer(f"<b>Котик, я тебя не понимаю( Лучше воспользуйся меню❤</b>", reply_markup=keyboards.start_kb)    


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())


