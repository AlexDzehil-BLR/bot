import datetime
import matplotlib.pyplot as plt
import requests
from dateutil import rrule


# a = '20210405'
# b = datetime.datetime.today().strftime('%Y%m%d')
#
#
# x_usd = []
# x_eur = []
# y_usd = []
# y_eur = []
# for dt in rrule.rrule(rrule.DAILY,
#     dtstart=datetime.datetime.strptime(a, '%Y%m%d'),
#     until=datetime.datetime.strptime(b, '%Y%m%d')):
#     now = dt.strftime('%Y%m%d')
#     print(now[:4], now[4:6], now[6:8])
#
#     url_nbrb = f'https://www.nbrb.by/api/exrates/rates?ondate={now[:4]}-{now[4:6]}-{now[6:8]}&periodicity=0'
#     r = requests.get(url_nbrb)
#     day = now
#
#     usd, number_usd = r.json()[4]['Cur_Abbreviation'], r.json()[4]['Cur_OfficialRate']
#     eur, number_eur = r.json()[5]['Cur_Abbreviation'], r.json()[5]['Cur_OfficialRate']
#     y_usd.append(number_usd)
#     y_eur.append(number_usd)
#     x_usd.append(day)
#     x_eur.append(day)

# print(x_usd)
# print(y_usd)


def current_rate_plot_usd(month=0):
    # Курс доллара и евро по НБ РБ
    if month == 1:
        b = -30
    elif month == 6:
        b = -180
    elif month == 12:
        b = -365
    today = datetime.date.today().strftime('%Y%m%d')
    a = datetime.date.today()
    bb = datetime.timedelta(days=b)
    cc = a + bb
    format_time = str(cc)
    format = format_time.split('-')
    f = ''.join(format)
    print(f)
    x_usd = []
    y_usd = []
    for dt in rrule.rrule(rrule.DAILY,
        dtstart=datetime.datetime.strptime(f, '%Y%m%d'),
        until=datetime.datetime.strptime(today, '%Y%m%d')):
        now = dt.strftime('%Y%m%d')

        url_nbrb = f'https://www.nbrb.by/api/exrates/rates?ondate={now[:4]}-{now[4:6]}-{now[6:8]}&periodicity=0'
        r = requests.get(url_nbrb)
        day = dt.strftime('%m.%d')

        number_usd = r.json()[4]['Cur_OfficialRate']
        y_usd.append(number_usd)
        x_usd.append(day)
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.plot(x_usd, y_usd, linewidth=3)
    ax.set_title('График курса валют', fontsize=24)
    ax.tick_params(axis='both', labelsize=14)
    plt.show()


def current_rate_plot_eur(month=0):
    # Курс доллара и евро по НБ РБ
    if month == 1:
        b = -30
    elif month == 6:
        b = -180
    elif month == 12:
        b = -365
    today = datetime.date.today().strftime('%Y%m%d')
    a = datetime.date.today()
    bb = datetime.timedelta(days=b)
    cc = a + bb
    format_time = str(cc)
    format = format_time.split('-')
    f = ''.join(format)
    x_eur = []
    y_eur = []
    for dt in rrule.rrule(rrule.DAILY,
        dtstart=datetime.datetime.strptime(f, '%Y%m%d'),
        until=datetime.datetime.strptime(today, '%Y%m%d')):
        now = dt.strftime('%Y%m%d')

        url_nbrb = f'https://www.nbrb.by/api/exrates/rates?ondate={now[:4]}-{now[4:6]}-{now[6:8]}&periodicity=0'
        r = requests.get(url_nbrb)
        day = dt.strftime('%m.%d')

        number_eur = r.json()[5]['Cur_OfficialRate']
        y_eur.append(number_eur)
        x_eur.append(day)
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.plot(x_eur, y_eur, linewidth=3)
    ax.set_title('График курса валют', fontsize=24)
    ax.tick_params(axis='both', labelsize=14)
    plt.show()


current_rate_plot_eur(1)




