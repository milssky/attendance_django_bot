from datetime import datetime
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_bot.settings')
django.setup()

from telegram import Update
from telegram.ext import CallbackContext

from attendance.models import Course, Student
from tgbot.handlers.onboarding import static_text
from tgbot.handlers.onboarding.keyboard import make_keyboard_for_start_command


def command_start(update: Update, context: CallbackContext) -> None:
    text = static_text.start_success_text.format(first_name=update.effective_user.username)
    update.message.reply_text(text=text)


def command_email(update: Update, context: CallbackContext) -> None:
    command, email = update.message.text.split(' ')
    # TODO валидация email
    try:
        student = Student.objects.get(email=email)
        text = static_text.email_success.format(first_name=student.name)
        update.message.reply_text(text=text, reply_markup=make_keyboard_for_start_command(student))
    except Student.DoesNotExist:
        update.message.reply_text(text=static_text.email_wrong.format(email=email))


def course_handler(update: Update, context: CallbackContext) -> None:
    course_name, student_id = update.callback_query.data.split("-")
    course = Course.objects.get(name=course_name)
    student = Student.objects.get(pk=student_id)


    context.bot.send_message(
        text=update.callback_query.data,
        chat_id=update.effective_user.id
    )
