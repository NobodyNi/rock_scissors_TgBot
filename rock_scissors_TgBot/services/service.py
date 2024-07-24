import random
from rock_scissors_TgBot.lexicon.lexicon_ru import LEXICON_RU, COUNTER


def get_bot_choice() -> str:
    game = ['rock', 'scissors', 'paper', 'lizard', 'spock']
    return random.choice(game)


def _normalize_user_answer(user_answer: str) -> str:
    for i in LEXICON_RU:
        if LEXICON_RU[i] == user_answer:
            break
    return i


def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules = {
        'rock': ['scissors', 'lizard'],
        'scissors': ['paper', 'lizard'],
        'paper': ['rock', 'spock'],
        'spock': ['scissors', 'rock'],
        'lizard': ['paper', 'spock']
    }
    if bot_choice == user_choice:
        COUNTER['draw'] += 1
        COUNTER['total_games'] += 1
        return 'nobody_won'
    elif bot_choice in rules[user_choice]:
        COUNTER['wins'] += 1
        COUNTER['total_games'] += 1
        return 'user_won'
    COUNTER['lose'] += 1
    COUNTER['total_games'] += 1
    return 'bot_won'
