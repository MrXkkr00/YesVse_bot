from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State

from data.config import group_id
from keyboards.default.startMenuKeys import menuStart_ru, only_menu_ru
from loader import dp, bot


class BuyurtmaState_ru(StatesGroup):
    photo = State()
    text = State()


@dp.message_handler(text="🏠Главное меню")
async def fadsfdsasdg_ru(message: types.Message, state: FSMContext):
    await message.answer(f"Привет!", reply_markup=menuStart_ru)


@dp.message_handler(text="🏠Главное меню", state=[BuyurtmaState_ru.photo, BuyurtmaState_ru.text])
async def fadsfdsag_ru(message: types.Message, state: FSMContext):
    await message.answer(f"Привет!", reply_markup=menuStart_ru)
    await state.finish()


@dp.message_handler(text="🇷🇺Русский язык")
async def uz_start_ru(message: types.Message):
    await message.answer(f"Привет! Пожалуйста, прочтите правила, чтобы узнать о боте, процессе заказа и другую "
                         f"информацию👇️")
    with open('./data/Правила есть всё.pdf', 'rb') as doc:
        await message.answer_document(document=doc,
                                      caption="Продолжая, вы подтверждаете, что прочитали правила и согласны с ними.",
                                      reply_markup=menuStart_ru)


@dp.message_handler(text="🛠Техническая поддержка")
async def yordam_ru(message: types.Message):
    await message.answer(f"Если у вас есть дополнительные вопросы: @estvsesupport_bot")


@dp.message_handler(text="ℹЧасто задаваемые вопросы")
async def kop_beriladigan_ru(message: types.Message):
    await message.answer(f"<b>Как заказать товар?</b>\n\n"

                         f"Оплата производится картой.\n\n"

                         f"Вы предоставляете изображение нужного вам товара и свою информацию о нем через кнопку "
                         f"«Оформить заказ», и бот ответит вам в ближайшее время, если товар вас устраивает, вы "
                         f"сделаете 50% предоплату и отправляете чек администратору, а остальной процесс будет продолжен "
                         f"с этим администратором бота.\n\n"

                         f"(Каждый чек проверяется по специальному коду чека)\n\n"

                         f"<b>Как долго товар будет на руках?</b>\n\n"
                         f"В зависимости от товара. Цена варьируется в зависимости от дня доставки.\n\n"

                         f"<b>Как устроена служба доставки?</b>\n\n"

                         f"Если вы находитесь в городе Ташкент, его доставят через Яндекс ГО или курьеры «Есть всЁ!». "
                         f"В регионы через почтовых служб таких как BTS или EMU.\n\n"

                         f"Стоимость доставки не входит в стоимость товара и оплачивается отдельно курьеру или "
                         f"почтовой службе, доставившей его.")


@dp.message_handler(text="🛍Оформить заказ")
async def fasdfefs_ru(message: types.Message):
    await message.answer(f"Отправьте фотографии товара, который хотите заказать", reply_markup=only_menu_ru)
    await BuyurtmaState_ru.photo.set()


@dp.message_handler(content_types='photo', state=BuyurtmaState_ru.photo)
async def photot_ru(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(
        {'photo_id': photo_id}
    )

    await message.answer(f"Напишите известную вам информацию о товаре.")
    await BuyurtmaState_ru.text.set()


@dp.message_handler(state=BuyurtmaState_ru.photo)
async def pghdsog_ru(message: types.Message):
    await message.answer(f"Отправьте фотографии товара, который хотите заказать")


@dp.message_handler(state=BuyurtmaState_ru.text)
async def adfad_ru(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    photo = data.get('photo_id')

    await message.answer(f"Ваш заказ принят, дождитесь ответа оператора", reply_markup=menuStart_ru)
    await state.finish()
    await bot.send_photo(chat_id=group_id, photo=photo, caption=f"{text}\n\n"
                                                                f"Mijoz : {message.from_user.full_name}\n"
                                                                f"User_name : @{message.from_user.username}\n"
                                                                f"user_id :{message.from_user.id}")
    # await message.reply_photo()
    # await bot.forward_message()
