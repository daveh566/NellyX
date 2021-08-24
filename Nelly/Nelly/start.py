from Nelly import NELLY
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

NELLY_START = """
Hello, I am Nelly chatbot, My master is @aspirer2 If You Are Feeling Lonely, You can Always Come to me and Chat With Me!
"""


@NELLY.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("Nelly", switch_inline_query_current_chat="nelly "), InlineKeyboardButton("Support", url = "https://t.me/KayAspirerProject")]
              ]
    await NELLY.send_message(chat_id = message.chat.id, text = NELLY_START, reply_markup = InlineKeyboardMarkup(buttons))
