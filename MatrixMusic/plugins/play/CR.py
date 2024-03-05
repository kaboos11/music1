import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/0395107f7b3d1e6ddda9f.jpg",
        caption=f"""\nمرحبا بك عزيزي {message.from_user.mention} في قسم سورس ميوزك\nللتحدث مع مطور السورس اضغط علي الازرار بالاسفل👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗴𝗿𝗼𝘂𝗽", url=f"https://t.me/NN_S3"), 
                 InlineKeyboardButton(
                   " 𝘀𝗼𝘂𝗿𝗰𝗲 𝗸𝗮𝗯𝗼𝗼𝘀",       url=f"https://t.me/KK_DX"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "𝗸𝗮𝗯𝗼𝗼𝘀 𝗯𝗮𝘀𝗵𝗮", url=f"https://t.me/Z_C_T"), 
                 
                ],

            ]

        ),

    )








@app.on_message(
    command(["مطور السورس","المبرمج","مبرمج"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("Z_C_T")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"𝘀𝗼𝘂𝗿𝗰𝗲 𝗸𝗮𝗯𝗼𝗼𝘀  \n\n‍ ¦𝗱𝗲𝘃 :{name}\n ¦𝘂𝘀𝗲𝗿 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦𝗕𝗜𝗢 :{usr.bio}\n\n𝘀𝗼𝘂𝗿𝗰𝗲 𝗸𝗮𝗯𝗼𝗼𝘀 ", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["كابوس"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("Z_C_T")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"𝘀𝗼𝘂𝗿𝗰𝗲 𝗸𝗮𝗯𝗼𝗼𝘀  .\n\n¦𝗱𝗲𝘃 :{name}\n ¦𝘂𝘀𝗲𝗿 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦𝗕𝗜𝗢 :{usr.bio}\n\n𝘀𝗼𝘂𝗿𝗰𝗲 𝗸𝗮𝗯𝗼𝗼𝘀", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



