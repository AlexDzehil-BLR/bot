import datetime

import matplotlib.pyplot as plt
import requests
from dateutil import rrule


def current_rate_plot_usd_month():
    # Курс доллара и евро по НБ РБ
    b = -30
    today = datetime.date.today().strftime('%Y%m%d')
    a = datetime.date.today()
    bb = datetime.timedelta(days=b)
    cc = a + bb
    format_time = str(cc)
    format = format_time.split('-')
    f = ''.join(format)
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
    ax.xaxis.set_major_locator(plt.MaxNLocator(15))
    ax.plot(x_usd, y_usd, linewidth=3)
    ax.set_title('График курса USD', fontsize=24)
    ax.tick_params(axis='both', labelsize=14)
    plt.savefig('image/usd_month.png')


def current_rate_plot_usd_6month():
    # Курс доллара и евро по НБ РБ
    b = -180
    today = datetime.date.today().strftime('%Y%m%d')
    a = datetime.date.today()
    bb = datetime.timedelta(days=b)
    cc = a + bb
    format_time = str(cc)
    format = format_time.split('-')
    f = ''.join(format)
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
    ax.xaxis.set_major_locator(plt.MaxNLocator(20))
    ax.plot(x_usd, y_usd, linewidth=3)
    ax.set_title('График курса USD', fontsize=24)
    ax.tick_params(axis='both', labelsize=14)
    plt.savefig('image/usd_6month.png')


def current_rate_plot_eur_month():
    # Получим период построения графика
    b = -30
    # Высчитаем начальную дату
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
    ax.xaxis.set_major_locator(plt.MaxNLocator(15))
    ax.plot(x_eur, y_eur, linewidth=3)
    ax.set_title('График курса EUR', fontsize=24)
    ax.tick_params(axis='both', labelsize=14)
    plt.savefig('image/eur_month.png')


def current_rate_plot_eur_6month():
    # Получим период построения графика
    b = -180
    # Высчитаем начальную дату
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
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))

    ax.plot(x_eur, y_eur, linewidth=3)
    ax.set_title('График курса EUR', fontsize=24)
    ax.tick_params(axis='both', labelsize=14)
    plt.savefig('image/eur_6month.png')



current_rate_plot_eur_month()
current_rate_plot_usd_month()
current_rate_plot_eur_6month()
current_rate_plot_usd_6month()