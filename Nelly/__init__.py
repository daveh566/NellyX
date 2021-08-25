from Nelly.config import Config
from pyrogram import Client

API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN

NELLY = Client(':memory:', api_id=API_ID, api_hash=API_HASH, token=TOKEN)
