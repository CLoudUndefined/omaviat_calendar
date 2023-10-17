import os

import dotenv

from omaviat_calendar.bot import TelegramBot

dotenv.load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = TelegramBot(BOT_TOKEN)
