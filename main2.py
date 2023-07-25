import os
from FinamPy.Config import Config

from finam_trade_api.client import Client
from finam_trade_api.candles.model import (
    DayCandlesRequestModel, 
    DayInterval, 
    IntraDayCandlesRequestModel, 
    IntraDayInterval
)

from finam_trade_api.order.model import (
    BoardType,
    CreateOrderRequestModel,
    CreateStopOrderRequestModel,
    DelOrderModel,
    OrdersRequestModel,
    OrderType,
    PropertyType,
    StopLossModel,
    StopQuantity,
    StopQuantityUnits,
    TakeProfitModel
)

token = Config.AccessToken

async def get_day_candles():
    client = Client(token)
    params = DayCandlesRequestModel(
        securityBoard="FUT",
        securityCode='USDRUBF',
        timeFrame=DayInterval.D1,
        intervalFrom="2023-07-10",
        intervalTo="2023-07-13",
    )

    return await client.candles.get_day_candles(params)

if __name__ == "__main__":
    import asyncio
    client = Client(token)
    
    # print(asyncio.run(client.securities.get_data('USDRUBF')))
    # print(asyncio.run(client.securities.get_data('SiU3')))
    # code='USDRUBF' board='FUT' market='Forts' decimals=2.0 lotSize=1.0 minStep=1.0 currency='RUR' instrumentCode='F' shortName='USDRUBF' properties=255.0 timeZoneName='Russian Standard Time' bpCost=1000.0000000000002 accruedInterest=0.0 priceSign='Any' ticker='' lotDivider=1.0


    print(asyncio.run(get_day_candles()))
