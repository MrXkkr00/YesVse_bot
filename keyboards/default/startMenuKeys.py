from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛍️Buyurtma berish'),
        ],
        [
            KeyboardButton(text="ℹKo'p beriladigan savollar"),
            KeyboardButton(text='🛠Texnoyordam'),
        ],
    ],
    resize_keyboard=True
)


menuStart_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛍Оформить заказ'),
        ],
        [
            KeyboardButton(text="ℹЧасто задаваемые вопросы"),
            KeyboardButton(text='🛠Техническая поддержка'),
        ],
    ],
    resize_keyboard=True
)


til = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿O'zbek tili"),
            KeyboardButton(text="🇷🇺Русский язык"),
        ],
    ], resize_keyboard=True
)

only_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🏠Bosh menu')
        ]
    ], resize_keyboard=True
)

only_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🏠Главное меню')
        ]
    ], resize_keyboard=True
)