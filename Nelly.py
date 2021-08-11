Upprint("[INFO]: Importing Your API_ID, API_HASH, BOT_TOKEN")
import re
from asyncio import (gather, get_event_loop, sleep)

from aiohttp import ClientSession
from pyrogram import filters
from Python_ARQ import ARQ

from config import bot, BOT_TOKEN, ARQ_API_KEY, ARQ_API_BASE_URL, LANGUAGE
bot_token= BOT_TOKEN

print("[INFO]: Checking... Your Details")

bot_id = int(bot_token.split(":")[0])
print("[INFO]: Code running by master Prince Op")
arq = None


async def lunaQuery(query: str, user_id: int):
    query = (
        query
        if LANGUAGE == "en"
        else (await arq.translate(query, "en")).result.translatedText
    )
    resp = (await arq.luna(query, user_id)).result
    return (
        resp
        if LANGUAGE == "en"
        else (
            await arq.translate(resp, LANGUAGE)
        ).result.translatedText
    )


async def type_and_send(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, "typing")
    response, _ = await gather(lunaQuery(query, user_id), sleep(2))
    if "Luna" in response:
        responsee = response.replace("Luna", "Nelly")
    else:
        responsee = response
    if "Aco" in responsee:
        responsess = responsee.replace("Aco", "Nelly")
    else:
        responsess = responsee
    if "Who is Tiana?" in responsess:
        responsess2 = responsess.replace("Who is Nelly?", "Heroine Of Telegram")
    else:
        responsess2 = responsess
    await message.reply_text(responsess2)
    await message._client.send_chat_action(chat_id, "cancel")


@bot.on_message(filters.text & ~filters.private & ~filters.edited & ~filters.bot & ~filters.via_bot & ~filters.channel & ~filters.forwarded)
async def nelly(client, message):
    chat_id = message.chat.id
    if not message.reply_to_message:
        message.continue_propagation()
    try:
        aibot = message.reply_to_message.from_user.id
    except:
        return
    if aibot != BOT_ID:
        message.continue_propagation()
    text = message.text

    if text.startswith("/") or text.startswith("@"):
        message.continue_propagation()
    try:
        lan = translator.detect(text)
    except:
        return
    test = text
    if not "en" in lan and not lan == "":
        try:
            test = translator.translate(test, lang_tgt="en")
        except:
            return
    finaltxt = test.replace(" ", "%20")
    try:
        L = await fetch(f"https://api.affiliateplus.xyz/api/chatbot?message={finaltxt}&botname=Nelly&ownername=Aspirer&user=1")
        msg = L["message"]        
    except Exception as e:
        await m.edit(str(e))
        return
    if not "en" in lan and not lan == "":
        msg = translator.translate(msg, lang_tgt=lan[0])
    try:
        await bot.send_chat_action(message.chat.id, "typing")
        await message.reply(msg)
    except:
        return
    message.continue_propagation()

    
@bot.on_message(filters.command("start") & ~filters.edited)
async def start(client, message):
   if message.chat.type == 'private':
       await message.reply("**Hey There, I'm Nelly. An advanced chatbot with AI. \n\nAdd me to your group and chat with me!**",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Dev", url="https://t.me/KayAspirerProject"),
                                        InlineKeyboardButton(
                                            "Repo", url="https://t.me/KayAspirerProject")
                                    ]]
                            ),               
           )
   else:

       await message.reply("**I'm alive, check my pm to know more about me!**")

bot.run()
