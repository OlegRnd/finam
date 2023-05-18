# import time
# # 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
# token = "CAEQ1ZACGhjrE64no9apCjdI6k+dMfQso3wM6TKzq9U="
# cid = "757282RDVBT"

# from FinamRestPy import *

# fr = FinamRestPy(client_id=cid, access_token=token)
# res = fr.get_securities()

# # print(res['securities'])
# # quit()

# for i in res['securities']:
#     if (i['code'].lower() == 'sim3'):
#         print(i)


from FinamPy.FinamPy import FinamPy
from FinamPy.Config import Config


if __name__ == '__main__':  # Точка входа при запуске этого скрипта
    fp_provider = FinamPy(Config.AccessToken)  # Подключаемся

    symbols = (('TQBR', 'SBER'), ('FUT', 'SiM3'), ('FUT', 'RIM3'))  # Кортеж тикеров в виде (код площадки, код тикера)

    print('Получаем информацию обо всех тикерах (займет несколько секунд)...')
    
    res = fp_provider.subscribe_order_book('SiM3','FUT')

    # Проверяем работу подписок
    print(f'\nПодписка на стакан тикера: FUT.SiM3')
    print('ask - минимальная цена покупки, bid - максимальная цена продажи')
    fp_provider.on_order_book = lambda order_book: print('ask:', order_book.asks[0].price, 'bid:', order_book.bids[0].price)  # Обработчик события прихода подписки на стакан
    # fp_provider.subscribe_order_book(security_code, security_board, 'orderbook1')  # Подписываемся на стакан тикера   

    input('Enter - выход\n')
    res = fp_provider.unsubscribe_order_book(res,'SiM3','FUT')
    fp_provider.close_channel()
    quit()

    securities = fp_provider.get_securities()  # Получаем информацию обо всех тикерах
    # print('Ответ от сервера:', securities)
    for board, symbol in symbols:  # Пробегаемся по всем тикерам
        try:
            si = next(item for item in securities.securities if item.board == board and item.code == symbol)
            # print(si)
            print(f'\nИнформация о тикере {si.board}.{si.code} ({si.short_name}, {fp_provider.markets[si.market]}):')
            print(f'Валюта: {si.currency}')
            decimals = si.decimals
            print(f'Кол-во десятичных знаков: {decimals}')
            print(f'Лот: {si.lot_size}')
            min_step = 10 ** -decimals * si.min_step
            print(f'Шаг цены: {min_step}')
        except:
            print(f'\nТикер {board}.{symbol} не найден')

    fp_provider.close_channel()  # Закрываем канал перед выходом
