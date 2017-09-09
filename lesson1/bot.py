import ephem
import datetime
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    updater = Updater("432283548:AAFcJ8EIaghmH2SyvDBy5Ngn892-6INbTZ8")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constellation, pass_args = True))
    dp.add_handler(CommandHandler("wordcount", word_count, pass_args = True))
    dp.add_handler(CommandHandler("calculate", calculate, pass_args = True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    text = 'Приветствую тебя, {}!'.format(update['message']['chat']['first_name'])
    #print(update)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    #print(user_text)
    update.message.reply_text(user_text)

planets = {
    'марс': ephem.Mars,
    'меркурий' : ephem.Mercury,
    'венера' : ephem.Venus,
    'юпитер' : ephem.Jupiter,
    'сатурн' : ephem.Saturn,
    'уран' : ephem.Uranus,
    'нептун' : ephem.Neptune
}

def planet_constellation(bot, update, args):
    user_text = update.message.text
    #print(user_text)
    if len(args) > 0:
        user_text = args[0].lower()
        now = datetime.datetime.now()
        planet = planets.get(user_text)
        if planet:
            answer = ephem.constellation(planet(str(now)))
            update.message.reply_text(answer[1])
        else:
            update.message.reply_text('А ты уверен(а) что это вообще планета?')
    else:
        update.message.reply_text('Ты не ввел(а) название планеты!')

def word_count(bot, update, args):
    if len(args) > 0:
        update.message.reply_text('В данной фразе {} слов(а)'.format(len(args)))
    else:
        update.message.reply_text('Хэй, а фразу-то ты не ввел(а)!')

def calculate(bot, update, args):
    if len(args) > 0:
        command = ''.join(args)
        answer = None
        try:
            if command.find('+') != -1:
                args_list = command.split('+')
                if len(args_list) == 2:
                    answer = int(args_list[0]) + int(args_list[1])
            elif command.find('-') != -1:
                args_list = command.split('-')
                if len(args_list) == 2:
                    answer = int(args_list[0]) - int(args_list[1])
            elif command.find('/') != -1:
                args_list = command.split('/')
                if len(args_list) == 2:
                    try:
                        answer = int(args_list[0]) / int(args_list[1])
                    except ZeroDivisionError:
                        answer = 'Деление на 0 все еще не разрешено!'
            elif command.find('*') != -1:
                args_list = command.split('*')
                if len(args_list) == 2:
                    answer = int(args_list[0]) * int(args_list[1])
            else:
                answer = 'Не могу распознать такое математическое выражение:('
            if answer == None:
                answer = 'ДВУХ ЧИСЕЛ ДВУХ ДВУХ ЧИСЕЛ, НЕ ТРЕХ, НЕ ЧЕТЫРЕХ, А ДВУХ МАТЬ ЕГО ДВУХ ЧИСЕЛ'
        except (ValueError, TypeError):
            answer = 'Эммм что-то не то ты ввел, дружок' 
        update.message.reply_text(str(answer))
    else:
        update.message.reply_text('Нечего рассчитывать!')


main()