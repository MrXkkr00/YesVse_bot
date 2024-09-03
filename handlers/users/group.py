from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ContentType

from data.config import group_id, ADMINS
from keyboards.default.startMenuKeys import menuStart, only_menu
from loader import dp, bot


@dp.message_handler(lambda message: message.reply_to_message is not None)
async def get_reply_text(message: types.Message):
    try:
    # reply_text = message.reply_to_message # Reply qilingan xabarning texti
    # user_id = message.reply_to_message.from_user.id
        text = message.reply_to_message.caption
        x = text.split(':')
        mijoz_user_id = x[-1]

        photo = message.reply_to_message.photo[-1]

        await bot.send_photo(photo=photo.file_id, chat_id=mijoz_user_id, caption=f"<b>ADMIN</b>\n"
                                                                                 f"{message.text}", parse_mode="HTML")
        await message.reply(f"Xabar yuborildi")


    except:
        await bot.send_message(chat_id=ADMINS[0], text=f"group.py textda xato")


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_replfdfstext(message: types.Message):
    try:
        if message.reply_to_message:
            # Rasmni olish
            photo_id = message.photo[-1].file_id
            # caption = message.photo[-1].caption
            text = message.reply_to_message.caption
            x = text.split(':')
            mijoz_user_id = x[-1]

            photo = message.reply_to_message.photo[-1]
            await bot.send_photo(photo=photo.file_id, chat_id=mijoz_user_id)
            await bot.send_photo(photo=photo_id, chat_id=mijoz_user_id, caption=f"<b>ADMIN</b>\n"
                                                                                f"{message.caption}", parse_mode="HTML")
            await message.reply(f"Xabar yuborildi")
        else:
            await message.reply("Bu xabar faqat reply qilingan xabarlarga ruxsat etiladi.")
    except:
        await bot.send_message(chat_id=ADMINS[0], text=f"group.py photoda xato")
