from aiogram import Router
from aiogram.types import Message
from rock_scissors_TgBot.lexicon.lexicon_ru import LEXICON_RU

router = Router()


@router.message()
async def process_send_message(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
