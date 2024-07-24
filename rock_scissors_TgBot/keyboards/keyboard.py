from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from rock_scissors_TgBot.lexicon.lexicon_ru import LEXICON_RU

button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

button_1 = KeyboardButton(text=LEXICON_RU['rock'])
button_2 = KeyboardButton(text=LEXICON_RU['scissors'])
button_3 = KeyboardButton(text=LEXICON_RU['paper'])
button_4 = KeyboardButton(text=LEXICON_RU['lizard'])
button_5 = KeyboardButton(text=LEXICON_RU['spock'])

game_kb_builder = ReplyKeyboardBuilder()

game_kb_builder.row(button_1, button_2, button_3,
                    button_4, button_5, width=2)

game_kb: ReplyKeyboardMarkup = game_kb_builder.as_markup(
    resize_keybboard=True
)
