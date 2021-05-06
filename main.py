"""Бот курсов валют"""
import datetime
import requests

from telegram.ext import Updater


API_KEY = '1618613141:AAHWGYgMfWBDTyPjpTZ4IiTdXl7kzDXvMzA'


def main():
    mybot = Updater(API_KEY, use_context=True)

    mybot.start_polling()
    mybot.idle()


def current_rate():
    # Сегодняшнее число
    print(datetime.date.today())
    # Курс доллара и евро по НБ РБ
    url_nbrb = 'https://www.nbrb.by/api/exrates/rates?periodicity=0'
    r = requests.get(url_nbrb)
    print('***НБ РБ***')
    print(r.json()[4]['Cur_Abbreviation'], '-->', r.json()[4]['Cur_OfficialRate'])
    print(r.json()[5]['Cur_Abbreviation'], '-->', r.json()[5]['Cur_OfficialRate'])

    # Курс валют по Беларусбанк
    url_belarusbank = 'https://belarusbank.by/api/kursExchange?city=Слоним'
    r_belb = requests.get(url_belarusbank)
    print('***Беларусбанк***')
    print('USD', r_belb.json()[0]['USD_in'], r_belb.json()[0]['USD_out'])
    print('EUR', r_belb.json()[0]['EUR_in'], r_belb.json()[0]['EUR_out'])

    # # Курс валют в Белагропромбанке
    url_belagroprom = f'https://belapb.by/CashExRatesDaily.php?ondate={datetime.date.today().day}/{datetime.date.today().month}/{datetime.date.today().year}'
    print('https://belapb.by/CashExRatesDaily.php?ondate=7/5/2020')
    r_belagroprom = requests.get(url_belagroprom)
    print(r_belagroprom.status_code)


main()
