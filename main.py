import asyncio

from aiogram import Router, Bot, Dispatcher
from aiogram.types import BotCommand

from bot.handlers.commands import commands_register
from bot.utils.config_reader import config
from bot.utils.database.postgres import DataBase


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Start this bot"),
    ]
    await bot.set_my_commands(commands)


async def start_up():
    default_router = Router()
    # Создаем экземпляр бота, передаем токен, устанавливаем мод кодировки.
    bot = Bot(token=config.token, parse_mode="HTML")
    # Создаем экземпляр диспатчера бота.
    dp = Dispatcher()
    # Привязываем к нему роутер.
    dp.include_router(default_router)

    commands_register(default_router)
    await set_bot_commands(bot)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), config=config)


if __name__ == '__main__':
    try:
        loop = asyncio.new_event_loop()
        loop.run_until_complete(start_up())
        # loop.run_until_complete(DataBase.create_pool())
    except (KeyboardInterrupt, SystemExit):
        print('bot stopped')

