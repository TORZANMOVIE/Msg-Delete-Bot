import asyncio
import logging
from os import environ
from pyrogram import Client, filters
from pyrogram import utils as pyroutils
from aiohttp import web
from webcode import web_server
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

pyroutils.MIN_CHAT_ID = -999999999999
pyroutils.MIN_CHANNEL_ID = -100999999999999
logging.getLogger("asyncio").setLevel(logging.CRITICAL - 1)

PORT = environ.get("PORT", "8080")
API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))

GROUPS = [int(x) for x in environ.get("GROUPS").split()]
ADMINS = [int(x) for x in environ.get("ADMINS").split()]

START_MSG = "<b>Hai {},\nI'm a private bot of @cinemabasar to delete group messages after a specific time</b>"

User = Client(
    name="user-account",
    session_string=SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    workers=300
)

Bot = Client(
    name="auto-delete",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    workers=300
)

# ➤ /start handler for bot
@Bot.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    buttons = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Join Support", url="https://t.me/CinemaXpressGroup")]]
    )
    await message.reply(
        START_MSG.format(message.from_user.mention),
        reply_markup=buttons
    )

# ➤ Auto-delete handler in groups
@User.on_message(filters.chat(GROUPS))
async def auto_delete(user, message):
    try:
        if message.from_user.id in ADMINS:
            return
        await asyncio.sleep(TIME)
        await user.delete_messages(chat_id=message.chat.id, message_ids=message.id)
    except Exception as e:
        print(e)

# ➤ Main runner
async def main():
    await User.start()
    await Bot.start()

    me = await Bot.get_me()
    print(f"Bot started as @{me.username}")
    print("Both User and Bot started!")

    # Start aiohttp web server for health check
    app = web.AppRunner(await web_server())
    await app.setup()
    await web.TCPSite(app, "0.0.0.0", int(PORT)).start()

    # Keep running until interrupted
    await asyncio.get_event_loop().create_future()

    # Cleanup on exit
    await Bot.stop()
    await User.stop()

# Start everything
asyncio.run(main())
