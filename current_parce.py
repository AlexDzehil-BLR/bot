import datetime
import requests


def print_date():
    return datetime.date.today()


def current_rate_nacbank():
    # Курс доллара и евро по НБ РБ
    url_nbrb = 'https://www.nbrb.by/api/exrates/rates?periodicity=0'
    r = requests.get(url_nbrb)
    usd, number_usd = r.json()[4]['Cur_Abbreviation'], r.json()[4]['Cur_OfficialRate']
    eur, number_eur = r.json()[5]['Cur_Abbreviation'], r.json()[5]['Cur_OfficialRate']
    text = f"***НБ РБ***\n{usd} {str(number_usd)}\n{eur} {str(number_eur)}"
    return text


def current_rate_belbank():
    # Курс валют по Беларусбанк
    url_belarusbank = 'https://belarusbank.by/api/kursExchange?city=Слоним'
    r_belb = requests.get(url_belarusbank)
    usd, number_usd_in, number_usd_out = 'USD', r_belb.json()[0]['USD_in'], r_belb.json()[0]['USD_out']
    eur, number_eur_in, number_eur_out = 'EUR', r_belb.json()[0]['EUR_in'], r_belb.json()[0]['EUR_out']
    text = f"***Беларусбанк***\n{usd} {str(number_usd_in)} {str(number_usd_out)}\n{eur} {str(number_eur_in)} {str(number_eur_out)}"
    return text


def current_rate_belbank_multiplay_usd(user_number):
    # Курс валют по Беларусбанк
    url_belarusbank = 'https://belarusbank.by/api/kursExchange?city=Слоним'
    r_belb = requests.get(url_belarusbank)
    number_usd_out = float(r_belb.json()[0]['USD_out'])
    return number_usd_out * user_number


def current_rate_belbank_multiplay_eur(user_number):
    # Курс валют по Беларусбанк
    url_belarusbank = 'https://belarusbank.by/api/kursExchange?city=Слоним'
    r_belb = requests.get(url_belarusbank)
    number_eur_out = float(r_belb.json()[0]['EUR_out'])
    return number_eur_out * user_number


def current_rate_belapb():
    # # Курс валют в Белагропромбанке
    url_belagroprom = f'https://belapb.by/CashExRatesDaily.php?ondate={datetime.date.today().day}/{datetime.date.today().month}/{datetime.date.today().year}'
    r_belagroprom = requests.get(url_belagroprom)
    print(r_belagroprom.status_code)
