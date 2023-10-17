import asyncio
import os

import dotenv

import omaviat_calendar.extensions
from omaviat_calendar.config import bot

dotenv.load_dotenv()

asyncio.run(bot.polling())
