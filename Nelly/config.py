import os

from heroku3 import from_key
from pyrogram import Client

API_ID = int(os.environ.get("API_ID", "6"))
API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
