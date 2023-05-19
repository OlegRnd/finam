import time

from FinamPy.FinamPy import FinamPy
from FinamPy.Config import Config


if __name__ == '__main__':  # Точка входа при запуске этого скрипта
    # fp_provider = FinamPy(Config.AccessToken)  # Подключаемся

    fp_provider = FinamPy(Config.AccessToken)  # Провайдер работает со всеми счетами по токену (из файла Config.py)
    # fp_provider2 = FinamPy(Config.AccessToken)  # Для каждого провайдера будет создан свой экземпляр FinamPy
    # print(f'\nЭкземпляры класса совпадают: {fp_provider2 is fp_provider}')
    # fp_provider2.close_subscriptions_thread()  # Второй провайдер больше не нужен. Закрываем его поток подписок

    security_board = 'FUT'  # Код площадки
    security_code = 'SiM3'  # Тикер

    # Проверяем работу запрос/ответ
    print(f'\nДанные тикера: {security_board}.{security_code}')
    securities = fp_provider.get_securities()  # Получаем информацию обо всех тикерах
    si = next(item for item in securities.securities if item.board == security_board and item.code == security_code)
    print(si)

    # Проверяем работу подписок
    print(f'\nПодписка на стакан тикера: {security_board}.{security_code}')
    print('ask - минимальная цена покупки, bid - максимальная цена продажи')
    fp_provider.on_order_book = lambda order_book: print('ask:', order_book.asks[0].price, 'bid:', order_book.bids[0].price)  # Обработчик события прихода подписки на стакан
    fp_provider.subscribe_order_book(security_code, security_board, 'orderbook1')  # Подписываемся на стакан тикера

    # Выход
    input('Enter - выход\n')
    fp_provider.unsubscribe_order_book('orderbook1', 'SBER', 'TQBR')  # Отписываемся от стакана тикера
    fp_provider.close_channel()  # Закрываем канал перед выходом


    # symbols = (('TQBR', 'SBER'), ('FUT', 'SiM3'), ('FUT', 'RIM3'))  # Кортеж тикеров в виде (код площадки, код тикера)

    
    # res = fp_provider.subscribe_order_book('SBER', 'TQBR')

    # # Проверяем работу подписок
    # print(f'\nПодписка на стакан тикера: FUT.SiM3 (идентификатор: {res})')
    # print('ask - минимальная цена покупки, bid - максимальная цена продажи')
    # fp_provider.on_order_book = lambda order_book: print('ask:', order_book.asks[0].price, 'bid:', order_book.bids[0].price)  # Обработчик события прихода подписки на стакан
    # # fp_provider.subscribe_order_book(security_code, security_board, 'orderbook1')  # Подписываемся на стакан тикера   

    # input('Enter - выход\n')

    # res = fp_provider.unsubscribe_order_book(res,'SiM3','FUT')
    # print('Exiting...')
    # fp_provider.close_channel()
    # quit()

    # securities = fp_provider.get_securities()  # Получаем информацию обо всех тикерах
    # # print('Ответ от сервера:', securities)
    # for board, symbol in symbols:  # Пробегаемся по всем тикерам
    #     try:
    #         si = next(item for item in securities.securities if item.board == board and item.code == symbol)
    #         # print(si)
    #         print(f'\nИнформация о тикере {si.board}.{si.code} ({si.short_name}, {fp_provider.markets[si.market]}):')
    #         print(f'Валюта: {si.currency}')
    #         decimals = si.decimals
    #         print(f'Кол-во десятичных знаков: {decimals}')
    #         print(f'Лот: {si.lot_size}')
    #         min_step = 10 ** -decimals * si.min_step
    #         print(f'Шаг цены: {min_step}')
    #     except:
    #         print(f'\nТикер {board}.{symbol} не найден')

    # fp_provider.close_channel()  # Закрываем канал перед выходом
