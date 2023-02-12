import json

from django.http import JsonResponse
from django.views import View
from telegram import Update

from attendance_bot.celery import app
from attendance_bot.settings import DEBUG
from tgbot.dispatcher import dispatcher
from tgbot.main import bot

@app.task(ignore_result=True)
def process_telegram_event(update_json):
    update = Update.de_json(update_json, bot)
    dispatcher.process_update(update)


def index(request):
    return JsonResponse({"error": "Wazzuuup, hacker!"})


class TelegramBotWebhookView(View):
    def post(self, request, *args, **kwargs):
        if DEBUG:
            process_telegram_event(json.loads(request.body))
        else:
            process_telegram_event.delay(json.loads(request.body))
        return JsonResponse({"ok": "POST received"})

    def get(self, request, *args, **kwargs):
        return JsonResponse({"ok": "chilling"})
