# bot.py
from pyromod import listen
from pyrogram import Client
from config import *

plugins = dict(root="plugins")

bot = Client(
    "FileStore",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=plugins,
    workers=100
)

print("Bot is starting...")
bot.run()
