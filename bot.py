import asyncio
from os import environ
from pyrogram import Client, filters, idle
from pyrogram import utils as pyroutils

pyroutils.MIN_CHAT_ID = -999999999999
pyroutils.MIN_CHANNEL_ID = -100999999999999

API_ID = int(27269324)
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(30)
GROUPS = ["-1002480654065 -1002031758791 -1002259621643 -1002592745366"].split()
ADMINS = [1355140465]

START_MSG = "<b>Hai {},\nI'm a private bot of @Freekzz_Botz \nUsed For Deleting Messages After Specific Time. \nContact @Freekzz_2008 To Gain Access.</b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started ")
Bot.start()
print("Bot Started")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
