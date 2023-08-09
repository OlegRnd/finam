import os
from datetime import timedelta, datetime, date
import pytz
import matplotlib.pyplot as plt

from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now

from Config.Config import Config


def week_hall_close_open():
    counter = 0
    cur_day = 19

    with Client(Config.Tinkoff['token']) as client:
        si_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_si'],

            from_=datetime(year=2023,month=7, day=cur_day,hour=10,minute=0,second=0,tzinfo=pytz.UTC),
            to=datetime(year=2023,month=7, day=cur_day,hour=23,minute=0,second=0,tzinfo=pytz.UTC),

            interval=CandleInterval.CANDLE_INTERVAL_1_MIN)
    
        rubf_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_rubf'],

            from_=datetime(year=2023,month=7, day=cur_day,hour=10,minute=0,second=0,tzinfo=pytz.UTC),
            to=datetime(year=2023,month=7, day=cur_day,hour=23,minute=0,second=0,tzinfo=pytz.UTC),

            interval=CandleInterval.CANDLE_INTERVAL_1_MIN)

        high = -10000
        low = 10000

        rubf = 0

        for si_candle in si_candles:
            counter +=1
            try: 
                rubf = next(rubf_candles)
            except Exception:
                continue
 
            
            rubf_open = rubf.open.units + rubf.open.nano / 1000000000
            rubf_close =  rubf.close.units + rubf.close.nano / 1000000000

            si_open = si_candle.open.units + si_candle.open.nano / 1000000000
            si_close = si_candle.close.units + si_candle.close.nano / 1000000000

            buf = 0
            if (rubf_open < rubf_close):
                buf = rubf_open
                rubf_open = rubf_close
                rubf_close = buf

            if (si_open < si_close):
                buf = si_open
                si_open = si_close
                si_close = buf

            high_buf = float(rubf_open) - float(si_open) / 1000
            low_buf = float(rubf_close) - float(si_close) / 1000
            
            if (high_buf > high): high = high_buf
            if (low_buf < low): low = low_buf   
        
        print("Открытие и закрытие свечей")
        print("Date: ", datetime(year=2023,month=7, day=cur_day))
        print("Максимум: ", round(high, 2))
        print("Минимум: ", round(low, 2))
        print(counter)

    return 0


def week_hall_high_low():

    av_si = {}
    av_rubf = {}

    cur_day = date.today().day

    start = datetime(year=2023, month=date.today().month, day=cur_day, hour=9, minute=0, second=0,tzinfo=pytz.UTC)
    end = datetime(year=2023, month=date.today().month, day=cur_day, hour=22, minute=0, second=0,tzinfo=pytz.UTC)

    with Client(Config.Tinkoff['token']) as client:
        si_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_si'],
            from_=start,
            to=end,
            interval=CandleInterval.CANDLE_INTERVAL_1_MIN)
    
        rubf_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_rubf'],
            from_=start,
            to=end,
            interval=CandleInterval.CANDLE_INTERVAL_1_MIN)

        for si_candle in si_candles:
            av_si[int(si_candle.time.strftime("%Y%m%d%H%M%S"))] = (si_candle.high.units / 1000 + si_candle.low.units / 1000) * 0.5

        for rubf_candle in rubf_candles:
            av_rubf[int(rubf_candle.time.strftime("%Y%m%d%H%M%S"))] = (rubf_candle.high.units + rubf_candle.high.nano / 1000000000 + rubf_candle.low.units + rubf_candle.low.nano / 1000000000) * 0.5

    print(av_si)
    quit()

    si_buf = 0
    rubf_buf = 0

    av_spred = {}

    for i in range(int((start).strftime("%Y%m%d%H%M%S")),
                    int((end).strftime("%Y%m%d%H%M%S"))):
        if (i in av_rubf):
            rubf_buf = av_rubf[i]
        if (i in av_si):
            si_buf = av_si[i]           
        av_spred[i] = round(si_buf - rubf_buf, 2)

    spred_graf = plt.plot(list(range(0, len(av_spred))),
    # plt.plot(x_list, 
                av_spred.values())

    plt.xlabel('Время')
    plt.ylabel('Спред')
    
    plt.setp(spred_graf[0],linewidth=0.8)

    # plt.plot(list(range(0, len(spred_low))), 
    #          spred_low.values())

    # plt.scatter(list(range(0, len(spred_high))),
    #             spred_high.values())
    plt.grid()
    plt.show()   

    return 0

def main():
    week_hall_high_low()
    # week_hall_close_open()
    return 0

if __name__ == "__main__":
    main()




# HistoricCandle(open=Quotation(units=90092, nano=0), 
#                high=Quotation(units=90436, nano=0), low=Quotation(units=88507, nano=0), 
#                close=Quotation(units=88709, nano=0), volume=1119769, 
#                time=datetime.datetime(2023, 7, 10, 4, 0, tzinfo=datetime.timezone.utc), is_complete=True)
