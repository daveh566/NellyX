import os
from urllib.parse import unquote, urlparse
import re
import traceback
import sys
import random
import aiohttp
import requests
import traceback
from Nelly import NELLY
from datetime import datetime
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    CallbackQuery,
    InlineQuery,
    InlineQueryResultAnimation,
)   
from pykeyboard import InlineKeyboard

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
    return data


@NELLY.on_inline_query()
async def inline_query_handler(client, query):
    string = query.query.lower()

    answers = []
    if string.split()[0] == "nelly":
            if len(string.split()) < 2:
                await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text='Nelly | Chat [text]',
                    switch_pm_parameter='nelly',
                )
                return
            nell = string.split(None, 1)[1].strip()
            Nelly = await Nelly(answers, nelly)
            await client.answer_inline_query(
                query.id,
                results=Nelly,
                cache_time=2
            )
   

async def Nelly(answers, text):
    URL = f"https://api.affiliateplus.xyz/api/chatbot?message={text}&botname=@nelly&ownername=@aspirer2"
    result = await fetch(URL)
    buttons = InlineKeyboard(row_width=1)
    buttons.add(InlineKeyboardButton(
        "Nelly",
        switch_inline_query_current_chat="nelly"
    ))
    caption = f"""
**You:** `{text}`
**Nelly:** `{result['message']}`"""
    answers.append(
        InlineQueryResultPhoto(
            photo_url="https://telegra.ph/file/8e413b21ebcda0e52f3e8.jpg",
            caption=caption,
            reply_markup=buttons
        ))
    return answers
