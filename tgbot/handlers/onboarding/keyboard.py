import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_bot.settings')
django.setup()

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from attendance.models import Course, Student


def make_keyboard_for_start_command(student: Student) -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton(course.name, callback_data=f"{course.name}-{student.pk}") for course in student.courses.all()
    ]]
    return InlineKeyboardMarkup(buttons)

