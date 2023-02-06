from telegram import Update
from telegram.ext import CallbackContext

from tgbot.handlers.onboarding import static_text
from tgbot.handlers.onboarding.keyboard import make_keyboard_for_start_command


def command_start(update: Update, context: CallbackContext) -> None:
    text = static_text.start_success_text.format(first_name=update.effective_user.username)
    update.message.reply_text(text=text, reply_markup=make_keyboard_for_start_command())
