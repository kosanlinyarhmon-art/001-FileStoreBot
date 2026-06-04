import sys
import logging
import traceback
import time
import os
from aiohttp import web
import pyromod
from pyrogram import Client
from config import *

# Logging စတင်ခြင်း
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Web Server အတုလေး (Render အတွက်)
async def handle(request):
    return web.Response(text="Bot is running!")

app = web.Application()
app.router.add_get('/', handle)

# Bot Client
plugins = dict(root="plugins")
bot = Client(
    "FileStore",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=plugins,
    workers=100
)

async def run_bot():
    await bot.start()
    logger.info("Bot started successfully!")
    # idle() က Bot ကို အမြဲတမ်း ပွင့်နေအောင် လုပ်ပေးတယ်
    await bot.idle()

if __name__ == "__main__":
    try:
        logger.info("Bot is starting...")
        
        # Web server ကို စတင်ခြင်း (Render port error မတက်အောင်)
        runner = web.AppRunner(app)
        async def start_web():
            await runner.setup()
            site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get('PORT', 8080)))
            await site.start()
            
        import asyncio
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_web())
        
        # Bot ကို run ခြင်း
        loop.run_until_complete(run_bot())
        
    except Exception:
        logger.error("Error detected:")
        traceback.print_exc()
