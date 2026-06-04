import asyncio
import sys
import logging
from pyrogram import Client
from config import *

# Logging စတင်ခြင်း
logging.basicConfig(level=logging.INFO)

# Pyromod ကို import လုပ်စရာမလိုပါ၊ ရိုးရိုး Pyrogram client ပဲသုံးပါ
# Pyromod က install လုပ်ထားရင် သူ့ဘာသာအလုပ်လုပ်သွားပါလိမ့်မယ်

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
        # Error အသေးစိတ်ကို မြင်ရအောင် traceback ကိုလည်း ထည့်စစ်နိုင်ပါတယ်
        print(f"Error detected: {e}")
