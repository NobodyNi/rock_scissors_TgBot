from aiogram import Bot
from aiogram.types import BotCommand
from rock_scissors_TgBot.lexicon.lexicon_ru import LEXICON_COMMANDS


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command=key, description=value) for key, value in LEXICON_COMMANDS.items()
    ]

    await bot.set_my_commands(main_menu_commands)

