import logging

import settings
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from current_parce import print_date, current_rate_nacbank, current_rate_belbank, current_rate_belbank_multiplay_usd, \
    current_rate_belbank_multiplay_eur

logging.basicConfig(filename='bot.log', level=logging.INFO)


def start_bot(update, context):
    update.message.reply_text("""Бот курса валют.
Напишите цифру и валюту в формате EUR или USA в которую хотите сконвертировать рубли. Например 100 USA.""",
                              reply_markup=main_keyboard())


def get_course(update, context):
    date = str(print_date())
    nacbank = current_rate_nacbank()
    belbank = current_rate_belbank()
    update.message.reply_text(f"{date}\n{nacbank}\n{belbank}", reply_markup=main_keyboard())


def rate(update, context):
    current_list_usd = ('usd', 'USD', 'доллар', 'долларов', 'баксов')
    current_list_eur = ('eur', 'EUR', 'евро', 'евриков')
    if len(context.args) == 2:
        try:
            user_number = float(context.args[0])
        except (TypeError, ValueError):
            message = 'Введите число.'
        else:
            if context.args[1] in current_list_usd:
                value = current_rate_belbank_multiplay_usd(user_number)
                message = f"{value} BY"
            elif context.args[1] in current_list_eur:
                value = current_rate_belbank_multiplay_eur(user_number)
                message = f"{value} EUR"
            else:
                message = 'Неправильно выбрана валюта.'
    else:
        message = 'Введите цифру и валюту. Например 100 usd или 100 eur.'
    update.message.reply_text(message)


def main_keyboard():
    return ReplyKeyboardMarkup([['Получить курс', 'График за месяц'],
                                ['Подписаться на уведомления', 'Отписаться от уведомлений']], resize_keyboard=True)


def get_plot(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open('image/usd_month.png', 'rb'))
    context.bot.send_photo(chat_id=chat_id, photo=open('image/eur_month.png', 'rb'))



def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', start_bot))
    dp.add_handler(CommandHandler('rate', rate))
    dp.add_handler(MessageHandler(Filters.regex('^(Получить курс)$'), get_course))
    dp.add_handler(MessageHandler(Filters.regex('^(График за месяц)$'), get_plot))
    dp.add_handler(MessageHandler(Filters.text, start_bot))

    logging.info('БОТ СТАРТОВАЛ!')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
