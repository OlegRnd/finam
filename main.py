import time

from FinamPy.FinamPy import FinamPy
from Config.Config import Config

Si = 0
Rubf = 0
SpreadPercent = 0
SpreadMoney = 0


def on_order_book(order_book):
    global Si
    global Rubf
    global SpreadMoney, SpreadPercent

# order_book - входящий параметр - информация с сервера
 
    # Раз в секунду приходят данные по стакану каждого инструмента, на который есть подписка
    # Задача: произвести расчет спреда, используя bid-ask данные
    # будет два варианта расчета, в зависимости от того, в какой части "песочных часов" мы находимся

    # constriction - сужение
    # enlargement - расширение    

    match order_book.security_code:
        case 'USDRUBF':
            print ('USDRUBF:')
            Rubf = float(order_book.bids[0].price)
        case 'SiM6':
            Si = float(order_book.bids[0].price) / 1000
            print ('SiM6')

    if (Rubf > 0 and Si > 0) :
        SpreadPercent = Si  * 100 / Rubf - 100
        SpreadMoney = Si - Rubf

        # Вариант 1 - на сужение спреда: Si стремится к RubF
        # Условия - спред больше чем 0.5р
        # Si - продаем (движется навстречу RubF)
        # Rubf - покупаем (движется навстречу Si)        
        if (SpreadMoney > 0.5):
            # открытие сделки:
              # Покупка USDRUBF (обязательно первая операция)
              # Продажа Si (вторая операция)

            # закрытие сделки:
              # Продажа USDRUBF
              # Покупка Si

            print ('Сужение спреда. Спред: ', SpreadMoney)

        if (SpreadMoney < 0.1):
            # достаточный спред - 20 копеек
            print ('Расширение спреда. Спред: ', SpreadMoney)

    print ('Rubf: ', Rubf,
            'Si:', Si,
            'Спред в %: ', SpreadPercent, 
            'Спред в рублях: ', SpreadMoney)
    


    return 

if __name__ == '__main__':  # Точка входа при запуске этого скрипта
 
    futures_provider = FinamPy(Config.AccessToken)  # Провайдер работает со всеми счетами по токену (из файла Config.py)
    futures_provider.on_order_book = lambda order_book: on_order_book(order_book)
 
    # security_board = Config.FuturesBoard  # Код площадки
    # security_code = Config.FutSeptember23  # Тикер - фьючерс на июнь

    # Проверяем работу подписок
    print(f'\nПодписка на стакан тикеров: {Config.FuturesBoard}.{Config.FutSeptember23} | {Config.FuturesBoard}.{Config.FutUsdRubf}')
    print('ask - минимальная цена покупки, bid - максимальная цена продажи')
    
    # futures_provider.subscribe_order_book(Config.FutSeptember23, Config.FuturesBoard, 'orderbook1')  # Подписываемся на стакан тикера
    futures_provider.subscribe_order_book(Config.FutUsdRubf, Config.FuturesBoard, 'orderbook2')  # Подписываемся на стакан тикера
 



    # Выход
    input('Enter - выход\n')
    # futures_provider.unsubscribe_order_book('orderbook1', Config.FutSeptember23, Config.FuturesBoard)  # Отписываемся от стакана тикера
    futures_provider.unsubscribe_order_book('orderbook2', Config.FutUsdRubf, Config.FuturesBoard)  # Отписываемся от стакана тикера
    futures_provider.close_channel()  # Закрываем канал перед выходом