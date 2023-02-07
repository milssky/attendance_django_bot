from datetime import datetime
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_bot.settings')
django.setup()

from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from attendance.models import Course, Schedule, Student
from tgbot.handlers.onboarding import static_text
from tgbot.handlers.onboarding.keyboard import make_keyboard_for_start_command
from tgbot.helpers import check_dates, clear_data
from tgbot.validators import validate_email


def command_start(update: Update, context: CallbackContext) -> None:
    text = static_text.start_success_text.format(
        first_name=update.effective_user.username,
        parse_mode=ParseMode.MARKDOWN_V2
    )
    update.message.reply_text(text=text, parse_mode=ParseMode.MARKDOWN_V2)


def command_email(update: Update, context: CallbackContext) -> None:
    try:
        command, email = update.message.text.split()
    except ValueError:
        update.message.reply_text(text=static_text.email_empty)
        return
    email = clear_data(email)
    if not validate_email(email):
        update.message.reply_text(text=static_text.email_error_format)
        return
    try:
        student = Student.objects.get(email=email)
        text = static_text.email_success.format(first_name=student.name)
        update.message.reply_text(text=text, reply_markup=make_keyboard_for_start_command(student))
    except Student.DoesNotExist:
        update.message.reply_text(text=static_text.email_wrong.format(email=email), parse_mode=ParseMode.MARKDOWN_V2)


def course_handler(update: Update, context: CallbackContext) -> None:
    course_name, student_id = update.callback_query.data.split("-")
    course = Course.objects.get(name=course_name)
    student = Student.objects.get(pk=student_id)
    schedules = course.schedule_set.all()
    now = datetime.now()
    for schedule in schedules:
        if not check_dates(now, schedule.lecture_datetime):
            context.bot.send_message(
                text=static_text.schedule_error_day.format(
                    time=now.time().strftime("%H:%m"),
                    day=now.date().strftime("%d.%m.%Y"),
                    course=course.name
                ),
                chat_id=update.effective_user.id
            )
            return

    context.bot.send_message(
        text=static_text.schedule_success.format(course=course.name),
        chat_id=update.effective_user.id
    )
