import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_bot.settings')
django.setup()

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from attendance.models import Course


def make_keyboard_for_start_command() -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton(course.name, callback_data=course.pk) for course in Course.objects.all()
    ]]
    return InlineKeyboardMarkup(buttons)

