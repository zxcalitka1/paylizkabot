from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButtonPollType
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData



start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Информация"),
            KeyboardButton(text="Ссылки")
        ],
        [
            KeyboardButton(text="Тарифы"),
            KeyboardButton(text="Спец.кнопки")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)



links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Лсик лизки🥰", url="tg://resolve?domain=HEALTyXA"),
            InlineKeyboardButton(text="Телеграмм канал📣", url="tg://resolve?domain=lizzkazots")
        ]
    ]
)


class Pagination(CallbackData, prefix="pag"):
    action: str
    page: int


def paginator(page: int=0):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅", callback_data=Pagination(action="prev", page=page).pack()),
        InlineKeyboardButton(text="➡", callback_data=Pagination(action="next", page=page).pack()),
        width=2
    )
    return builder.as_markup()


xotelki_kb =  InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Хотелки❤", url="tg://resolve?domain=hfgjhdfgjn")
        ]
    ]
)

spec_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="заказать Рекламу"),
            KeyboardButton(text="Стать Спонсором")
        ],
        [
            KeyboardButton(text="Хотелки"),
            KeyboardButton(text="Игрулька")
        ],
        [
             KeyboardButton(text="ВЕРНУТЬСЯ")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)


