from telegram.ext import CommandHandler, Dispatcher, CallbackQueryHandler

from tgbot.handlers.onboarding import handlers as onboarding_handlers


def setup_dispatcher(dp: Dispatcher):
    dp.add_handler(CommandHandler("start", onboarding_handlers.command_start))
    dp.add_handler(CommandHandler("email", onboarding_handlers.command_email))
    dp.add_handler(CallbackQueryHandler(onboarding_handlers.course_handler))
    return dp