#crushe

import asyncio
import logging
from pyromod import listen
from pyrogram import Client
# In Pyrogram 2.0, ParseMode is in enums
from pyrogram.enums import ParseMode
from config import API_ID, API_HASH, BOT_TOKEN
from telethon.sync import TelegramClient


loop = asyncio.get_event_loop()

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)

# Use a different session name
sex = TelegramClient('telethon_bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

app = Client(
    "RestrictBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=10,
    sleep_threshold=20,
    parse_mode=ParseMode.HTML,
    workdir="."
)

async def restrict_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await app.start()
    from pyrogram.types import BotCommand
    await app.set_bot_commands([
        BotCommand("start", "Launch the application"),
        BotCommand("batch", "Download in bulk"),
        BotCommand("login", "Login process to userbot"),
        BotCommand("logout", "Logout and clear data"),
        BotCommand("myplan", "View your personalized plan"),
        BotCommand("stats", "Display statistics and insights")
    ])
    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name


loop.run_until_complete(restrict_bot())


