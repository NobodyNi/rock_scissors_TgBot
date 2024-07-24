from collections import defaultdict

LEXICON_RU: dict[str, str] = {
    '/start': '<b>Привет!</b>\nДавай с тобой сыграем в игру '
              '"Камень, ножницы, бумага, ящерица, Спок"?\n\nЕсли ты, вдруг, '
              'забыл правила, команда /help тебе поможет!\n\n<b>Играем?</b>',
    '/help': 'Это очень простая игра. Мы одновременно должны '
             'сделать выбор одного из трех предметов. Камень, '
             'ножницы, бумага, ящерица или Спок.\n\nЕсли наш выбор '
             'совпадает - ничья, а в остальных случаях ножницы '
             'режут бумагу. Бумага заворачивает камень. Камень '
             'давит ящерицу, а ящерица травит Спока, в то время '
             'как Спок ломает ножницы, которые, в свою очередь, '
             'отрезают голову ящерице, которая ест бумагу, на которой '
             'улики против Спока. Спок испаряет камень, а камень, разумеется, '
             'затупляет ножницы. \n\n<b>Играем?</b>',
    'rock': 'Камень 🗿',
    'paper': 'Бумага 📜',
    'scissors': 'Ножницы ✂',
    'lizard': 'Ящерица 🦎',
    'spock': 'Спок 🖖',
    'yes_button': 'Давай!',
    'no_button': 'Не хочу!',
    'other_answer': 'Извини, увы, это сообщение мне непонятно...',
    'yes': 'Отлично! Делай свой выбор!',
    'no': 'Жаль...\nЕсли захочешь сыграть, просто разверни '
          'клавиатуру и нажми кнопку "Давай!"',
    'bot_won': 'Я победил!\n\nСыграем еще?',
    'user_won': 'Ты победил! Поздравляю!\n\nДавай сыграем еще?',
    'nobody_won': 'Ничья!\n\nПродолжим?',
    'bot_choice': 'Мой выбор',
    'statistic': '<b>Твоя статистика</b> 📊',
    'stat': 'Статистика 📊'
}

COUNTER = defaultdict(int, {'wins': 0, 'lose': 0, 'draw': 0, 'total_games': 0})

