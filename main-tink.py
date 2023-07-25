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

    cur_day = date.today().day - 1

    counter = 0
    high_list = []
    low_list = []
    x_list = []

    with Client(Config.Tinkoff['token']) as client:
        si_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_si'],

            from_=datetime(year=2023, month=7, day=cur_day,
                           hour=10, minute=0, second=0,
                           tzinfo=pytz.UTC),
            to=datetime(year=2023, month=7, day=cur_day,
                        hour=23, minute=0, second=0,
                        tzinfo=pytz.UTC),

            interval=CandleInterval.CANDLE_INTERVAL_1_MIN)
    
        rubf_candles = client.get_all_candles(
            figi=Config.Tinkoff['figi_rubf'],

            from_=datetime(year=2023, month=7, day=cur_day,
                           hour=10, minute=0, second=0,
                           tzinfo=pytz.UTC),
            to=datetime(year=2023, month=7, day=cur_day,
                        hour=23, minute=0, second=0,
                        tzinfo=pytz.UTC),

            interval=CandleInterval.CANDLE_INTERVAL_1_MIN)

        for si_candle in si_candles:
            print(type(si_candle.time))
            # high_list[si_candle.time] = 1


        # print(high_list)

        # high = -10000
        # low = 10000

        # rubf = 0

        # for si_candle in si_candles:
        #     counter += 1
        #     try: 
        #         rubf = next(rubf_candles)
        #     except Exception:
        #         continue
 
        #     rubf_high = rubf.high.units + rubf.high.nano / 1000000000
        #     rubf_low =  rubf.low.units + rubf.low.nano / 1000000000

        #     si_high = si_candle.high.units + si_candle.high.nano / 1000000000
        #     si_low = si_candle.low.units + si_candle.low.nano / 1000000000

        #     high_buf = float(rubf_high) - float(si_high) / 1000
        #     low_buf = float(rubf_low) - float(si_low) / 1000
            
        #     if (high_buf > high): high = high_buf
        #     if (low_buf < low): low = low_buf   
            
        #     high_list.append(round(high_buf, 2))
        #     low_list.append(round(low_buf, 2))
        #     x_list.append(rubf.time)

        # print("Максимум / минимум свечи")
        # print("Date: ", datetime(year=2023,month=7, day=cur_day))
        # print("Максимум: ", round(high, 2))
        # print("Минимум: ", round(low, 2))
        # print(counter)

        # x_list = list(range(0, len(high_list)))

        # print(len(high_list))

        # plt.bar(x_list, high_list)
        # plt.bar(x_list, low_list)

        # plt.show()

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
