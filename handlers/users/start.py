from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import group_id
from keyboards.default.startMenuKeys import menuStart, only_menu
from loader import dp, bot


# -1002157475452

class BuyurtmaState(StatesGroup):
    photo = State()
    text = State()


@dp.message_handler(text="🏠Bosh menu")
async def fadsfdsag(message: types.Message, state: FSMContext):
    await message.answer(f"Assalomu Alaykum", reply_markup=menuStart)


@dp.message_handler(text="🏠Bosh menu", state=[BuyurtmaState.photo, BuyurtmaState.text])
async def fadsfdsag(message: types.Message, state: FSMContext):
    await message.answer(f"Assalomu Alaykum", reply_markup=menuStart)
    await state.finish()


@dp.message_handler(text="🇺🇿O'zbek tili")
async def uz_start(message: types.Message):
    await message.answer(f"Assalomu aleykum! Bot, buyurtma jarayoni va boshqa ma'lumotlarni bilib olish uchun "
                         f"qoidalarni o'qib chiqing👇️")
    with open('./data/Hammasi bor qoidalari.pdf', 'rb') as doc:
        await message.answer_document(document=doc,
                                      caption="Davom etish orqali siz shartlarni o‘qib chiqqanligingizni va "
                                              "roziligingizni tasdiqlaysiz.",
                                      reply_markup=menuStart)


@dp.message_handler(text="🛠Texnoyordam")
async def yordam(message: types.Message):
    await message.answer(f"Qo'shimcha savollaringiz bo'lsa @estvsesupport_bot ga yozing")


@dp.message_handler(text="ℹKo'p beriladigan savollar")
async def kop_beriladigan(message: types.Message):
    await message.answer(f"<b>Qanday holda mahsulot buyurtma qilinadi?</b>\n\n"

                         f"'Buyurtma berish' tugmasi orqali kerak bo'lgan mahsulotingiz rasmi va u haqida "
                         f"ma'lumotingizni berasiz va bot sizga yaqin vaqt orasida javob beradi, mahsulot sizni "
                         f"qoniqtirsa 50% olindan to'lov qilasiz va qolgan jarayon admin bilan davom ettiriladi.\n\n"

                         f"(Har bir chek admin tomonidan maxsus chekdagi kod orqali tekshirib olinadi) \n\n"

                         f"To'lov karta orqali bajariladi.\n\n"

                         f"<b>Qancha vaqt ichida mahsulot qo'limida bo'ladi?</b>\n\n"
                         f"Qanday mahsulotligiga qarab. Narxi yetkazib berish kuniga qarab o'zgaradi.\n\n"

                         f"<b>Yetkazib berish xizmati qanday holda amalga oshiriladi?</b>\n\n"
                         f"Toshkent shaxrida joylashgan bo'lsangiz Yandex GO yoki 'Hammasi bor' kuryerlari tomonidan "
                         f"yetkazib beriladi. Viloyatlarga bo'lsa BTS yoki EMU kabi po'chta xizmatlaridan.\n\n"
                         f"Yetkazib berish narxi mahsulot narxiga aloqasi yo'q va aloxida yetkazib bergan kuryer "
                         f"yoki pochta servisiga to'lanadi.")


@dp.message_handler(text="🛍️Buyurtma berish")
async def fasdfefs(message: types.Message):
    await message.answer(f"Buyurtma bermoqchi bo’lgan mahsulotingizni sur’atini jo’nating", reply_markup=only_menu)
    await BuyurtmaState.photo.set()


@dp.message_handler(content_types='photo', state=BuyurtmaState.photo)
async def photot(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(
        {'photo_id': photo_id}
    )

    await message.answer(f"Mahsuolat haqida bilgan ma’lumotingizni yozing.")
    await BuyurtmaState.text.set()


@dp.message_handler(state=BuyurtmaState.photo)
async def pghdsog(message: types.Message):
    await message.answer(f"Buyurtma bermoqchi bo’lgan mahsulotingizni sur’atini jo’nating")


@dp.message_handler(state=BuyurtmaState.text)
async def adfad(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    photo = data.get('photo_id')

    await message.answer(f"Buyurtmangiz qabul qilindi iltimos operatorlar javobini kuting", reply_markup=menuStart)
    await state.finish()
    await bot.send_photo(chat_id=group_id, photo=photo, caption=f"{text}\n\n"
                                                                f"Mijoz : {message.from_user.full_name}\n"
                                                                f"User_name : @{message.from_user.username}\n"
                                                                f"user_id :{message.from_user.id}")
    # await message.reply_photo()
    # await bot.forward_message()
