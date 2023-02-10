import logging
import sys

import telegram
from telegram import Bot

from attendance_bot.settings import TG_BOT_TOKEN


bot = Bot(TG_BOT_TOKEN)
TELEGRAM_BOT_USERNAME = bot.get_me()["username"]

try:
    pass
except telegram.error.Unauthorized:
    logging.error("Неверный токен")
    sys.exit(1)
else:
    logging.info(f"Бот {TELEGRAM_BOT_USERNAME} запущен")
