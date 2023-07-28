#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 😎Creator😎 : <a href='https://t.me/Mister_Ash'>Ash Ketchum</a>\n○ 🥲Language🥲 : <code>Hindi</code>\n○ 😉Library😉 : <a href='https://docs.pyrogram.org/'>Indian library🇮🇳</a>\n○ 🥰Main Channel🥰 : <a href='https://t.me/The_Happy_Hour_Hindi'>The Happy Hour</a>\n○ 🥳Support Group🥳 : <a href='https://t.me/Happy_Hour_Hindi'>Click Here</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
