from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from rock_scissors_TgBot.lexicon.lexicon_ru import LEXICON_RU, COUNTER
from rock_scissors_TgBot.services.service import get_bot_choice, get_winner
from rock_scissors_TgBot.keyboards.keyboard import game_kb, yes_no_kb

router = Router()


@router.message(CommandStart())
async def process_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=yes_no_kb)


@router.message(Command(commands='help'))
async def process_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'],
                         reply_markup=yes_no_kb)


@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes(message: Message):
    await message.answer(text=LEXICON_RU['yes'],
                         reply_markup=game_kb)


@router.message(F.text == LEXICON_RU['no_button'])
async def process_no(message: Message):
    await message.answer(text=LEXICON_RU['no'])


@router.message(F.text == LEXICON_RU['stat'])
async def process_stat(message: Message):
    await message.answer(text=f'{LEXICON_RU['statistic']}\n\n'
                              f'Побед - {COUNTER['wins']}\n'
                              f'Поражений - {COUNTER['lose']}\n'
                              f'Ничьи - {COUNTER['draw']}\n'
                              f'Всего игр - {COUNTER['total_games']}',
                         reply_markup=yes_no_kb)


@router.message(F.text.in_([LEXICON_RU['rock'],
                            LEXICON_RU['scissors'],
                            LEXICON_RU['paper'],
                            LEXICON_RU['lizard'],
                            LEXICON_RU['spock']]))
async def process_game(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU['bot_choice']} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner],
                         reply_markup=yes_no_kb)
