"""Бот курсов валют"""
import requests


# Курс доллара и евро по НБ РБ
url_nbrb = 'https://www.nbrb.by/api/exrates/rates?periodicity=0'
r = requests.get(url_nbrb)
print(r.json()[4]['Cur_Abbreviation'], '-->', r.json()[4]['Cur_OfficialRate'])
print(r.json()[5]['Cur_Abbreviation'], '-->', r.json()[5]['Cur_OfficialRate'])

