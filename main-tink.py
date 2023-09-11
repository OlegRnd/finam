import os
from datetime import timedelta, datetime, date
import pytz
import matplotlib.pyplot as plt
from matplotlib import dates

from matplotlib.ticker import MultipleLocator

from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now

from Config.Config import Config

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def get_near_gold(start = 0, end = 0, interval = CandleInterval.CANDLE_INTERVAL_1_MIN):


    start = start or datetime(year=2023, month=date.today().month, day=date.today().day, hour=6, minute=0, second=0,tzinfo=pytz.UTC)
    end = end or datetime(year=2023, month=date.today().month, day=date.today().day, hour=23, minute=0, second=0,tzinfo=pytz.UTC)

    av_si = {}
    av_si2 = {}

    with Client(Config.Tinkoff['token']) as client:

        si_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_gold1'],
            from_=start,
            to=end,
            interval=interval)

        si2_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_gold2'],
            from_=start,
            to=end,
            interval=interval)

        # приходится прибавлять 3 часа ко времени графика. Почему то время считается по GMT+0
        for si_candle in si_candles:
            av_si[int(si_candle.time.strftime("%Y%m%d%H%M%S"))+30000] = (si_candle.high.units + si_candle.high.nano / 1000000000 + si_candle.low.units + si_candle.low.nano / 1000000000) * 0.5

        for si2_candle in si2_candles:
            av_si2[int(si2_candle.time.strftime("%Y%m%d%H%M%S"))+30000] = (si2_candle.high.units + si2_candle.high.nano / 1000000000 + si2_candle.low.units + si2_candle.low.nano / 1000000000) * 0.5


    return av_si, av_si2


def get_near_eur(start = 0, end = 0, interval = CandleInterval.CANDLE_INTERVAL_1_MIN):
  
    start = start or datetime(year=2023, month=date.today().month, day=date.today().day, hour=6, minute=0, second=0,tzinfo=pytz.UTC)
    end = end or datetime(year=2023, month=date.today().month, day=date.today().day, hour=23, minute=0, second=0,tzinfo=pytz.UTC)

    av_si = {}
    av_si2 = {}

    with Client(Config.Tinkoff['token']) as client:
        # resp = client.instruments.futures(instrument_status=1)
        # for r in resp.instruments:
        #     if ('NG' in r.ticker):
        #         print(r.figi)
        # quit()

        si_candles = client.get_all_candles(
            # figi=Config.Tinkoff['figi_ng1'],
            figi=Config.Tinkoff['figi_eur1'],
            from_=start,
            to=end,
            interval=interval)
    
        si2_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_eur2'],
            from_=start,
            to=end,
            interval=interval)

        for si_candle in si_candles:
            av_si[int(si_candle.time.strftime("%Y%m%d%H%M%S"))+30000] = (si_candle.high.units + si_candle.low.units) * 0.5

        for si2_candle in si2_candles:
            av_si2[int(si2_candle.time.strftime("%Y%m%d%H%M%S"))+30000] = (si2_candle.high.units + si2_candle.low.units) * 0.5

    return av_si, av_si2

def get_ng(start = 0, end = 0, interval = CandleInterval.CANDLE_INTERVAL_1_MIN):

    start = start or datetime(year=2023, month=8, day=11, hour=6, minute=0, second=0,tzinfo=pytz.UTC)
    end = end or datetime(year=2023, month=date.today().month, day=date.today().day, hour=23, minute=0, second=0,tzinfo=pytz.UTC)

    av_si = {}
    av_si2 = {}

    with Client(Config.Tinkoff['token']) as client:

        si_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_ng1'],
            from_=start,
            to=end,
            interval=interval)
    
        si2_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_ng2'],
            from_=start,
            to=end,
            interval=interval)

        for si_candle in si_candles:
            av_si[int(si_candle.time.strftime("%Y%m%d%H%M%S"))+30000] = (si_candle.high.units + si_candle.high.nano / 1000000000 + si_candle.low.units + si_candle.low.nano / 1000000000) * 0.5

        for si2_candle in si2_candles:
            av_si2[int(si2_candle.time.strftime("%Y%m%d%H%M%S"))+30000] = (si2_candle.high.units + si2_candle.high.nano / 1000000000 + si2_candle.low.units + si2_candle.low.nano / 1000000000) * 0.5


    return av_si, av_si2

# получение массива данных средних значений si и rubf 
# для расчета используются максимум и минимум свечи
def get_near_mxi(start = 0, end = 0, interval = CandleInterval.CANDLE_INTERVAL_1_MIN):

    start = start or datetime(year=2023, month=date.today().month, day=date.today().day, hour=6, minute=0, second=0,tzinfo=pytz.UTC)
    end = end or datetime(year=2023, month=date.today().month, day=date.today().day, hour=23, minute=0, second=0,tzinfo=pytz.UTC)

    av_si = {}
    av_si2 = {}

    with Client(Config.Tinkoff['token']) as client:
        # resp = client.instruments.futures(instrument_status=1)
        # for r in resp.instruments:
        #     if ('MX' in r.ticker):
        #         print(r.figi)
        # quit()

        si_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_mxi1'],
            from_=start,
            to=end,
            interval=interval)
    
        si2_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_mxi2'],
            from_=start,
            to=end,
            interval=interval)

        for si_candle in si_candles:
            av_si[int(si_candle.time.strftime("%Y%m%d%H%M%S"))+30000] = (si_candle.high.units + si_candle.high.nano / 1000000000 + si_candle.low.units + si_candle.low.nano / 1000000000) * 0.5

        for si2_candle in si2_candles:
            av_si2[int(si2_candle.time.strftime("%Y%m%d%H%M%S"))+30000] = (si2_candle.high.units + si2_candle.high.nano / 1000000000 + si2_candle.low.units + si2_candle.low.nano / 1000000000) * 0.5


    return av_si, av_si2

# получение массива данных средних значений si и rubf 
# для расчета используются максимум и минимум свечи
def get_near_usd_si(start = 0, end = 0, interval = CandleInterval.CANDLE_INTERVAL_1_MIN):

    start = start or datetime(year=2023, month=date.today().month, day=date.today().day, hour=6, minute=0, second=0,tzinfo=pytz.UTC)
    end = end or datetime(year=2023, month=date.today().month, day=date.today().day, hour=23, minute=0, second=0,tzinfo=pytz.UTC)

    av_si = {}
    av_si2 = {}

    with Client(Config.Tinkoff['token']) as client:
        # resp = client.instruments.futures(instrument_status=1)
        # for r in resp.instruments:
        #     if ('GD' in r.ticker):
        #         print(r.figi)

        # quit()

        si_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_usd_si'],
            from_=start,
            to=end,
            interval=interval)

        si2_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_usd_si2'],
            from_=start,
            to=end,
            interval=interval)

        # приходится прибавлять 3 часа ко времени графика. Почему то время считается по GMT+0
        for si_candle in si_candles:
            av_si[int(si_candle.time.strftime("%Y%m%d%H%M%S"))+30000] = (si_candle.high.units / 1000 + si_candle.low.units / 1000) * 0.5

        for si2_candle in si2_candles:
            av_si2[int(si2_candle.time.strftime("%Y%m%d%H%M%S"))+30000] = (si2_candle.high.units / 1000 + si2_candle.low.units / 1000) * 0.5

    return av_si, av_si2

# получение массива данных средних значений si и rubf 
# для расчета используются максимум и минимум свечи
def get_si_rubf(start = 0, end = 0, interval = CandleInterval.CANDLE_INTERVAL_1_MIN):

    start = start or datetime(year=2023, month=date.today().month, day=date.today().day, hour=6, minute=0, second=0,tzinfo=pytz.UTC)
    end = end or datetime(year=2023, month=date.today().month, day=date.today().day, hour=23, minute=0, second=0,tzinfo=pytz.UTC)

    av_si = {}
    av_rubf = {}

    with Client(Config.Tinkoff['token']) as client:
        si_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_usd_si'],
            from_=start,
            to=end,
            interval=interval)
    
        rubf_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_usd_rubf'],
            from_=start,
            to=end,
            interval=interval)

        # приходится прибавлять 3 часа ко времени графика. Почему то время считается по GMT+0
        for si_candle in si_candles:

            av_si[int(si_candle.time.strftime("%Y%m%d%H%M%S"))+30000] = (si_candle.high.units / 1000 + si_candle.low.units / 1000) * 0.5
            # av_si[int(si_candle.time.strftime("%Y%m%d%H%M%S"))] = (si_candle.high.units / 1000 + si_candle.low.units / 1000) * 0.5

        for rubf_candle in rubf_candles:
            av_rubf[int(rubf_candle.time.strftime("%Y%m%d%H%M%S"))+30000] = (rubf_candle.high.units + rubf_candle.high.nano / 1000000000 + rubf_candle.low.units + rubf_candle.low.nano / 1000000000) * 0.5
            # av_rubf[int(rubf_candle.time.strftime("%Y%m%d%H%M%S"))] = (rubf_candle.high.units + rubf_candle.high.nano / 1000000000 + rubf_candle.low.units + rubf_candle.low.nano / 1000000000) * 0.5

    return av_rubf, av_si

# построение графика ema на отрезке времени
# EMA в конкретной точке графика = (цена × вес цены) + (EMA в предыдущей точке графика × (1 − вес цены))
# Вес цены = 2 / (N + 1), где N — это количество временных отрезков, за который считается средняя, например, дней или часов. 

def spred_ema(start = 0, end = 0, n=7, interval = CandleInterval.CANDLE_INTERVAL_1_MIN):

    ema = []
    num_ema = 20
    price_weight = 2 / (num_ema + 1)

    time, av_spred = spred_hall(start, end, interval)
    
    ema.append(av_spred[0])
 
    for i in range(1, len(av_spred)):
        ema.append(av_spred[i] * price_weight + ema[i-1] * (1 - price_weight))

    return time, ema

# расчет данных для построения графика коридора спреда на заданом отрезке времени
def spred_hall(start = 0, end = 0, interval = CandleInterval.CANDLE_INTERVAL_1_MIN):

    # av_rubf, av_si = get_si_rubf(start, end, interval)
    # av_rubf, av_si = get_near_usd_si(start, end, interval)
    # av_rubf, av_si = get_near_mxi(start, end, interval)
    # av_rubf, av_si = get_ng(start, end, interval)
    av_rubf, av_si = get_ng()
    
    # av_rubf, av_si = get_near_eur(start, end, interval)
    # av_rubf, av_si = get_near_gold(start, end, interval)

    si_buf = 0
    rubf_buf = 0

    av_spred = []
    time_list=[]

    for i in av_si.keys():
        if (i in av_rubf):
            rubf_buf = av_rubf[i]
        if (i in av_si):
            si_buf = av_si[i]
        av_spred.append(round(si_buf - rubf_buf, 2))
        time_list.append(i)

    return time_list, av_spred 


def draw_plot(x_list, y_list, title='', x2_list=0, y2_list=0):

    fmt = dates.DateFormatter('%H:%M')

    spred_fig, spred_ax = plt.subplots()

    x_list = [datetime.strptime(str(i), "%Y%m%d%H%M%S") for i in x_list]
  
    spred_ax.xaxis.set_major_formatter(fmt)
    spred_fig.autofmt_xdate()
 
    spred_fig.set_figwidth(13)
    spred_fig.set_figheight(6)

    if (x2_list and y2_list):
        spred_graf = plt.plot(x_list, y_list, x_list, y2_list)
    else:
        spred_graf = plt.plot(x_list, y_list)
    
    plt.xlabel('Время')
    plt.ylabel('Спред')
    
    plt.setp(spred_graf[0],linewidth=1.2)
    plt.minorticks_on()
    plt.grid(which='major', color='#444', linewidth=1)
    plt.grid(which='minor', color='#aaa', ls=":")

    plt.title(title)

    plt.show()   

    return 0

def get_time_interval(term = 1):
    end = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=23, minute=0, second=0,tzinfo=pytz.UTC)
 
    match term:
        case 1:
            # график за сегодня - точнее за ближайший рабочий день (пн-пт)
            d = date.today().day if date.today().weekday() < 5 else date.today().day - (date.today().weekday() -  4)

            start = datetime(year=date.today().year, month=date.today().month, day=d, hour=6, minute=0, second=0,tzinfo=pytz.UTC)
            title = f"{start.strftime('%d %B %Y')}"

        case 2:
            # график за последние 3 дня
            d = date.today().day-2 if date.today().weekday() > 1 else (date.today().day-1 if date.today().weekday() == 1 else date.today().day)
            if (date.today().weekday() == 5):
                d = date.today().day - 3
            if (date.today().weekday() == 6):
                d = date.today().day - 4

            start = datetime(year=date.today().year, month=date.today().month, day=d, hour=6, minute=0, second=0,tzinfo=pytz.UTC)
            title = f"От {start.strftime('%Y-%m-%d')} до {end.strftime('%Y-%m-%d')}"

        case 3:
            # график за текущую неделю
            start = datetime(year=date.today().year, month=date.today().month, day=date.today().day-date.today().weekday(), hour=6, minute=0, second=0,tzinfo=pytz.UTC)

            title = f"От {start.strftime('%Y-%m-%d')} до {end.strftime('%Y-%m-%d')}"
        
        case 4:
            # график за последние 7 дней
            start = datetime(year=date.today().year, month=date.today().month, day=date.today().day-6, hour=6, minute=0, second=0,tzinfo=pytz.UTC)

            title = f"От {start.strftime('%Y-%m-%d')} до {end.strftime('%Y-%m-%d')}"


    return start, end, title

def main():

    interval = CandleInterval.CANDLE_INTERVAL_1_MIN

    term = int(input("Какой график строить?\n 1 - сегодня; 2 - последние 3 дня; 3 - текущая неделя; 4 - последние 7 дней; \n Выбор: "))

    # term = 1
    start, end, title = get_time_interval(term)

    x2_list, y2_list = spred_ema(start, end, interval)

    x_list, y_list = spred_hall(start, end, interval)


    draw_plot(x_list, y_list, title, x2_list, y2_list)

    # x_list, y_list = spred_hall(start, end, interval)
    # print(y_list)
    # draw_plot(x_list, y_list, title)

    return 0

if __name__ == "__main__":
    main()
