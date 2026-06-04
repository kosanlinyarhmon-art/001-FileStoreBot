import sys
import logging
import traceback
from pyrogram import Client
import pyromod # pyromod ကို import လုပ်ထားခြင်းက patching လုပ်ဖို့ အရေးကြီးပါတယ်
from config import *

# Logging စတင်ခြင်း
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

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
        logger.info("Bot is starting...")
        bot.run()
    except Exception:
        # Error တက်တဲ့နေရာကို အတိအကျဖော်ပြပေးမယ့် traceback ကို သုံးပါ
        logger.error("Error detected:")
        traceback.print_exc()
