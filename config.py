#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6111982752:AAH3VNBhcPvleKamxgLCGmwpCTEOiYxQw2M")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24579842"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ec6105bf1a02c98f837300546dc341d1")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001942168587"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1942168587"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://happythehour:skumar(2006)@cluster0.wttyshn.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "digitalreleasebot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "6"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>○ My Channel : <a href='https://t.me/The_Happy_Hour_Hindi'>The Happy Hour</a>\n○ My Group : <a href='https://t.me/Happy_Hour_Friends'>Click Here</a></b>\n\n\n<b><a href='https://t.me/The_Happy_Hour_Hindi'>👉 I love you Baby 😉😘🥰❤️💝</a></b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5379678669").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", """<a href='https://t.me/Movie_Ki_Duniya_Hindi'><b>CUSTOM_CAPTION</b></a>""")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "👉 मुजे मैसेज मत करों....😡 \nContact My Owner - <a href='https://t.me/Master_Jiraya'>🄼𝗮𝘀𝘁𝗲𝗿 𝗝𝗶𝗿𝗮𝘆𝗮</a>"

ADMINS.append(OWNER_ID)
ADMINS.append(1942168587)

LOG_FILE_NAME = "DigitalRelease.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
