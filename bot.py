# bot.py
import asyncio
import sys
import logging
from pyromod import listen
from pyrogram import Client
from config import *

# Logging စတင်ခြင်း
logging.basicConfig(level=logging.INFO)

# Event Loop စီစဉ်ခြင်း
if sys.platform != 'win32':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# Bot Client ဆောက်ခြင်း
plugins = dict(root="plugins")
bot = Client(
    "FileStore",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=plugins,
    workers=100
)

# Bot ကို Run ခြင်း
if __name__ == "__main__":
    try:
        print("Bot is starting...")
        bot.run()
    except Exception as e:
        print(f"Error detected: {e}")
