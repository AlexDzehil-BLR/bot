import datetime
import requests

from emoji import emojize
from xml.etree import ElementTree

emoji_list = [':date:', ':arrow_up:', ':arrow_down:', ':arrow_right:', ':x:']


def print_date():
    smile = emoji_list[0]
    smile = emojize(smile, use_aliases=True)
    format_date = f"{smile}{datetime.date.today().day}.{datetime.date.today().month}.{datetime.date.today().year}"
    return format_date


def current_rate_nacbank():
    # Курс доллара и евро по НБ РБ
    url_nbrb = 'https://www.nbrb.by/api/exrates/rates?periodicity=0'
    url_nbrb_yesterday = f'https://www.nbrb.by/api/exrates/rates?ondate={datetime.date.today().year}-{datetime.date.today().month}-{datetime.date.today().day-1}&periodicity=0'
    r = requests.get(url_nbrb)
    r_yest = requests.get(url_nbrb_yesterday)
    usd_yest, eur_yest = r_yest.json()[4]['Cur_OfficialRate'], r_yest.json()[5]['Cur_OfficialRate']
    # usd_yest, eur_yest = 1, 3
    smile_up = emojize(emoji_list[1], use_aliases=True)
    smile_down = emojize(emoji_list[2], use_aliases=True)
    smile_equal = emojize(emoji_list[3], use_aliases=True)
    usd, number_usd = r.json()[4]['Cur_Abbreviation'], r.json()[4]['Cur_OfficialRate']
    eur, number_eur = r.json()[5]['Cur_Abbreviation'], r.json()[5]['Cur_OfficialRate']
    #Евро упал доллар упал
    if eur_yest > number_eur and usd_yest > number_usd:
        return f"***НБ РБ***\n{usd} {smile_down} {str(number_usd)} | -{round((usd_yest-number_usd), 3)}\n{eur} {smile_down} {str(number_eur)} | -{round((eur_yest-number_eur), 3)}"
    #Евро упал доллар вырос
    elif eur_yest > number_eur and usd_yest < number_usd:
        return f"***НБ РБ***\n{usd} {smile_up} {str(number_usd)} | +{round((number_usd-usd_yest), 3)}\n{eur} {smile_down} {str(number_eur)} | -{round((eur_yest-number_eur), 3)}"
    #Евро вырос доллар упал
    elif eur_yest < number_eur and usd_yest > number_usd:
        return f"***НБ РБ***\n{usd} {smile_up} {str(number_usd)} | -{round((usd_yest-number_usd), 3)}\n{eur} {smile_down} {str(number_eur)} | +{round((number_eur-eur_yest), 3)}"
    #Евро вырос доллар вырос
    elif eur_yest < number_eur and usd_yest < number_usd:
        return f"***НБ РБ***\n{usd} {smile_up} {str(number_usd)} | +{round((number_usd-usd_yest), 3)}\n{eur} {smile_up} {str(number_eur)} | +{round((number_eur-eur_yest), 3)}"
    #Евро прежний доллар прежний
    elif eur_yest == number_eur and usd_yest == number_usd:
        return f"***НБ РБ***\n{usd} {smile_equal} {str(number_usd)}\n{eur} {smile_equal} {str(number_eur)}"
    #Евро вырос доллар прежний
    elif eur_yest < number_eur and usd_yest == number_usd:
        return f"***НБ РБ***\n{usd} {smile_equal} {str(number_usd)}\n{eur} {smile_up} {str(number_eur)} | +{round((number_eur-eur_yest), 3)}"
    #Евро прежний доллар вырос
    elif eur_yest == number_eur and usd_yest < number_usd:
        return f"***НБ РБ***\n{usd} {smile_up} {str(number_usd)} | +{round((number_usd-usd_yest), 3)}\n{eur} {smile_equal} {str(number_eur)}"
    #Евро упал доллар прежний
    elif eur_yest > number_eur and usd_yest == number_usd:
        return f"***НБ РБ***\n{usd} {smile_equal} {str(number_usd)}\n{eur} {smile_down} {str(number_eur)} | -{round((eur_yest-number_eur), 3)}"
    #Евро прежний доллар упал
    elif eur_yest == number_eur and usd_yest > number_usd:
        return f"***НБ РБ***\n{usd} {smile_down} {str(number_usd)} | -{round((usd_yest-number_usd), 3)}\n{eur} {smile_equal} {str(number_eur)}"
    # return text


def current_rate_belbank():
    # Курс валют по Беларусбанк
    url_belarusbank = 'https://belarusbank.by/api/kursExchange?city=Слоним'
    r_belb = requests.get(url_belarusbank)
    usd, number_usd_in, number_usd_out = 'USD', r_belb.json()[0]['USD_in'], r_belb.json()[0]['USD_out']
    eur, number_eur_in, number_eur_out = 'EUR', r_belb.json()[0]['EUR_in'], r_belb.json()[0]['EUR_out']
    text = f"***Беларусбанк***\n{usd} {str(number_usd_in)} {str(number_usd_out)}\n{eur} {str(number_eur_in)} {str(number_eur_out)}"
    return text


def current_rate_belbank_multiplay_usd(user_number):
    # Конверсия белрублей в доллары
    url_belarusbank = 'https://belarusbank.by/api/kursExchange?city=Слоним'
    r_belb = requests.get(url_belarusbank)
    number_usd_out = float(r_belb.json()[0]['USD_out'])
    multiplay = round((number_usd_out * user_number), 2)
    return multiplay


def current_rate_belbank_multiplay_eur(user_number):
    # Конверсия белрублей в евро
    url_belarusbank = 'https://belarusbank.by/api/kursExchange?city=Слоним'
    r_belb = requests.get(url_belarusbank)
    number_eur_out = float(r_belb.json()[0]['EUR_out'])
    multiplay = round((number_eur_out * user_number), 2)
    return multiplay


def current_rate_belapb():
    # # Курс валют в Белагропромбанке
    # url_belagroprom = f'https://belapb.by/CashExRatesDaily.php?ondate={datetime.date.today().day}/{datetime.date.today().month}/{datetime.date.today().year}'
    url_belagroprom = f'https://belapb.by/CashExRatesDaily.php?ondate=5/5/2021'
    r_belagroprom = requests.get(url_belagroprom)

    tree = ElementTree.parse(r_belagroprom.text)
    root = tree.getroot()
    for child in range(7):
        print(child)

