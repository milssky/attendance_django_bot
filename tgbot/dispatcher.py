from telegram.ext import CommandHandler, Dispatcher, CallbackQueryHandler

from attendance_bot.settings import DEBUG
from tgbot.handlers.onboarding import handlers as onboarding_handlers
from tgbot.main import bot



def setup_dispatcher(dp: Dispatcher):
    dp.add_handler(CommandHandler("start", onboarding_handlers.command_start))
    dp.add_handler(CommandHandler("email", onboarding_handlers.command_email))
    dp.add_handler(CallbackQueryHandler(onboarding_handlers.course_handler))
    return dp


n_workers = 0 if DEBUG else 4
dispatcher = setup_dispatcher(Dispatcher(bot, update_queue=None, workers=n_workers, use_context=True))
