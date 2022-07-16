from aiogram import Router
from aiogram.dispatcher.filters import Command

from bot.handlers.commands.start import start


def commands_register(router: Router):
    router.message.register(start, Command(commands='start'))