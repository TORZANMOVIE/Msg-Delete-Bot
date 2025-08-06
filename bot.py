import asyncio
from os import environ
from pyrogram import Client, filters, idle
from pyrogram import utils as pyroutils

pyroutils.MIN_CHAT_ID = -999999999999
pyroutils.MIN_CHANNEL_ID = -100999999999999

API_ID = int(27269324)
API_HASH ="986e6f78fd65198865ed61f81278ded8"
BOT_TOKEN ="8352433221:AAHU_MkT-iJqN_lwYFMkABXx1-iJ3IoQx04"
SESSION ="BQGgGMwAJErMs0BciAKlYLiXqFzd20vqu7UfcciEyN2TyRR_AjHS9xMG0hTXGtZ6Spnp3fOGY9P5dvixAL1yzCWfPu-Ksl5-DIk_iskMx4pGrgTSFD3DLPBbOOHJg74K_WEB4DoVD56ACAScfgH4gW7Nrb-p_bfPqtXpffzo35xjzuEU5rS2OG24xTXvGY_t6sJ8XTHV4rxG_MuHxWFBQFnDhSAope9zyFHWe0KovrqsEbCMRZHrldsDHdn4bCaH76LTG7XYTC0DKQqkuPCauOv_twIeDspIdDT6YeHkHIcQkqiO5T33gILEYSK0Gm_ZPboi3ymsdU_kC-th_alB-VHqdb0ZlAAAAABQxc1xAA"
TIME = int(30)
GROUPS = ["-1002480654065 -1002031758791 -1002259621643 -1002592745366"]
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
          await asyncio.sleep(10)
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
