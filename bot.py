# bot.py
from pyromod import listen
from pyrogram import Client
from config import *
import asyncio
import sys

# Event loop ပြဿနာကို ဖြေရှင်းရန်
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
else:
    # Render (Linux) အတွက် loop အသစ်တစ်ခု စတင်ပေးပါ
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from pyromod import listen
from pyrogram import Client
# ... ကျန်တဲ့ code များ ...

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
