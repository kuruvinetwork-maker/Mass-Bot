import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from info import Config, Txt


@Client.on_message(filters.private & filters.command('start'))
async def handle_start(bot: Client, message: Message):

    Btn = [
        [InlineKeyboardButton(text='⛑️ 𝖧ᴇʟᴘ 🚁', callback_data='help'), InlineKeyboardButton(text='🌀 𝖡ᴏᴛ sᴛᴀᴛᴜs ✳️', callback_data='server')],
        [InlineKeyboardButton(text='📰 𝖴ᴘᴅᴀᴛᴇs 🗞️', url='https://t.me/KURUVI_BABY'), InlineKeyboardButton(text='🤖 𝖡ᴏᴛ 𝐈ɴғᴏ ℹ️', callback_data='about')],
        [InlineKeyboardButton(text='🧑‍💻 𝖮ᴡɴᴇʀ ⌨️', user='https://t.me/KURUVI_TELE'),
    ]

    X = "https://files.catbox.moe/t5sqxa.jpg"
    Z = Txt.START_MSG.format(message.from_user.mention)

   
    await message.reply_photo(
        
        photo=X,
        caption=Z,
        reply_markup=InlineKeyboardMarkup(Btn)
    )
