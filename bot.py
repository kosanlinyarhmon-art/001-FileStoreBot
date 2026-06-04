# -*- coding: utf-8 -*-
import logging
from flask import Flask
from threading import Thread
from pyromod import listen
from pyrogram import Client
from config import *

# Flask setup
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

# Bot setup
plugins = dict(root="plugins")
bot = Client("FileStore",
             bot_token=BOT_TOKEN,
             api_id=API_ID,
             api_hash=API_HASH,
             plugins=plugins,
             workers=100)

if __name__ == "__main__":
    # Flask ကို Thread နဲ့ run
    Thread(target=run_flask).start()
    
    # Bot ကို run
    print("Bot is starting...")
    bot.run()
