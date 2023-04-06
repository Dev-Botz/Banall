import asyncio

from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import Client,filters
from pyrogram.types import *
from .config import Config
import logging
from pyrogram.errors import (
    ChatAdminRequired
)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if not Config.TELEGRAM_TOKEN:
   bot=Client(api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,session_name=Config.PYRO_SESSION)   
else:
   bot=Client(":memory:",api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,bot_token=Config.TELEGRAM_TOKEN)
   


@bot.on_message(filters.command("uban"))
async def mban(bot, msg):
    print("getting memebers from {}".format(msg.chat.id))
    async for i in bot.iter_chat_members(msg.chat.id):
        try:
            await bot.send_message(msg.chat.id, f"/ban {i.user.id}")
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print(" failed to kicked {} from {}".format(i.user.id,e))           
    print("process completed")

