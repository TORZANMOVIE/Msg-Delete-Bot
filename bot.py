import os
import asyncio
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from pyrogram.idle import idle

# Load environment variables from .env file
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_STRING = os.getenv("SESSION_STRING")
GROUPS = list(map(int, os.getenv("GROUPS", "").split()))
TIME = int(os.getenv("TIME", "10"))

# Initialize bot client (for user messages)
bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Initialize user client (to delete messages from other bots)
user = Client("user", session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH)

# Handler for messages sent by users (deleted by bot)
@bot.on_message(filters.group & filters.text)
async def delete_user_messages(_, message: Message):
    if message.chat.id in GROUPS and not message.from_user.is_bot:
        await asyncio.sleep(TIME)
        try:
            await message.delete()
        except Exception as e:
            print(f"❌ Failed to delete user message: {e}")

# Handler for messages sent by bots (deleted by user session)
@user.on_message(filters.group & filters.text)
async def delete_bot_messages(_, message: Message):
    if message.chat.id in GROUPS and message.from_user and message.from_user.is_bot:
        await asyncio.sleep(TIME)
        try:
            await message.delete()
        except Exception as e:
            print(f"❌ Failed to delete bot message: {e}")

User.start()
print("User oombi 🖕🏿")
Bot.start()
print("Bot oombi 🖕🏿")

idle()

User.stop()
print("User Stopped!😑")
Bot.stop()
print("Bot Stopped!😤")    
