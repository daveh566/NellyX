print("[INFO]: Importing Your API_ID, API_HASH, BOT_TOKEN")
import re
from asyncio import (gather, get_event_loop, sleep)
from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import (Client, filters, idle)
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
    if "Who is Nelly?" in responsess:
        responsess2 = responsess.replace("Who is Nelly?", "Heroine Of Telegram")
    else:
        responsess2 = responsess
    await message.reply_text(responsess2)
    await message._client.send_chat_action(chat_id, "cancel")


@bot.on_message(
    ~filters.private
    & filters.text
    & ~filters.command("start")
    & ~filters.edited,
    group=69,
)
async def chat(_, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    else:
        match = re.search(
            "[.|\n]{0,}iris[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match:
            return
    await type_and_send(message)


@bot.on_message(
    filters.private
    & ~filters.command("start")
    & ~filters.edited
)
async def chatpm(_, message):
    if not message.text:
        await message.reply_text("Ufff... Ignoring .... ¯\_(ツ)_/¯")
        return
    await type_and_send(message)


@bot.on_message(filters.regex("Nelly|nelly|NELLY"))
async def aspirer(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if (
        [(k) for k in u if k.startswith("@")]
        and [(k) for k in u if k.startswith("#")]
        and [(k) for k in u if k.startswith("/")]
        and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
    ):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        print(rm)

@bot.on_message(filters.command("start") & ~filters.edited)
async def startt(_, message):
    await message.reply_text("Hi, I'm Nelly My master is @aspirer2  inspired by  @kayaspirerproject group")


async def main():
    global arq
    session = ClientSession()
    arq = ARQ(ARQ_API_BASE_URL, ARQ_API_KEY, session)

    await bot.start()
    print(
        """
Nelly By Aspirer Is Deployed Successfully.
"""
    )
    await idle()


loop = get_event_loop()
loop.run_until_complete(main())
