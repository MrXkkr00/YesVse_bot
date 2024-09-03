from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards.default.startMenuKeys import til
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    # print(message.chat.id)
    f = open("./data/reklama.txt", "r")
    text = f.read()
    if not str(user_id) in text:
        f = open("./data/reklama.txt", "a")
        f.write(f"{user_id}\n")
        f.close()
    await message.delete()
    await message.answer(f"Привет {message.from_user.full_name}! Выберите язык 🇺🇿 🇷🇺\n"
                         f"Salom {message.from_user.full_name}! Til tanglang 🇺🇿 🇷🇺", reply_markup=til)


class Reklama_State(StatesGroup):
    text = State()


@dp.message_handler(text_contains="//reklama")
async def bot2342_start(message: types.Message, state: FSMContext):
    msg = message.text[9:]
    await state.update_data(
        {"msg": msg}
    )

    await message.answer(f"Rasm yuboring")
    await Reklama_State.text.set()


@dp.message_handler(content_types=["photo"], state=Reklama_State.text)
async def bot_text(message: types.Message, state: FSMContext):
    document_id = message.photo[0].file_id
    file_info = await bot.get_file(document_id)
    data = await state.get_data()
    msg = data.get("msg")
    f = open("./data/reklama.txt", "r")
    text = f.read()
    id = ""
    for i in range(len(text)):
        if not text[i] == f"\n":
            id += text[i]
        else:
            try:
                await bot.send_photo(chat_id=int(id), photo=file_info.file_id, caption=msg)
            except:
                id = ""
            id = ""
    await state.finish()


@dp.message_handler(text="//count")
async def bot22_start(message: types.Message):
    f = open("./data/reklama.txt", "r")
    text = f.read()
    sum = 0
    for i in range(len(text)):
        if text[i] == f"\n":
            sum = sum + 1
    await message.answer(f"{sum}")
