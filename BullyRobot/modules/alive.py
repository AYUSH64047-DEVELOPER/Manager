import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from BullyRobot.events import register
from BullyRobot import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/d41b53919d63247bd2b0d.png",
    "https://telegra.ph/file/d41b53919d63247bd2b0d.png",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ 𝗕𝗹𝗮𝗰𝗸 𝗦𝗼𝘃𝗲𝗿𝗲𝗶𝗴𝗻​**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝐉𝐨𝐡𝐧 𝐖𝐢𝐜𝐤](https://t.me/gtxPrime)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/BlackSovereignRoBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/BlackHarbour")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod
