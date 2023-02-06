from telegram.ext import CommandHandler, Dispatcher

from tgbot.handlers.onboarding import handlers as onboarding_handlers


def setup_dispatcher(dp: Dispatcher):
    dp.add_handler(CommandHandler("start", onboarding_handlers.command_start))
    return dp