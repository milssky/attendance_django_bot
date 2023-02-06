import os

import django
from telegram.ext import Updater

from attendance_bot.settings import TG_BOT_TOKEN
from tgbot.dispatcher import setup_dispatcher

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_bot.settings')
django.setup()


def run_polling(tg_token: str = TG_BOT_TOKEN):
    updater = Updater(tg_token, use_context=True)
    dp = updater.dispatcher
    dp = setup_dispatcher(dp)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    run_polling()
