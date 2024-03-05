from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𝗴𝗿𝗼𝘂𝗽", url= "https://t.me/NN_S3"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="مطور البوت", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="𝗴𝗿𝗼𝘂𝗽", url=f"https://t.me/NN_S3"), 
        ],
        [
            InlineKeyboardButton(text="مطور السورس", url=f"https://t.me/Z_C_T"), 
            InlineKeyboardButton(text="𝘀𝗼𝘂𝗿𝗰𝗲 𝗸𝗮𝗯𝗼𝗼𝘀", url=f"https://t.me/KK_DX") , 
        ],
    ]
    return buttons
