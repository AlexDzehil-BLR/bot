"""Бот курсов валют"""
import requests


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

