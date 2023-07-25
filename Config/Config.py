# токен для тинькова: "t.EkDLxnK0MfuXiGksuurwmiogYB2UC9B60pKlvNCoqF_EKPW2Fu8jq5546AB0p-CYFV9Db-9AoOn6ETpn8nsWtQ"
# токен для песочницы тинькоф: "t.ZOaxxirRwABb7BX9CKxq6KXSd4csHnFx0Sne0zR1WP8w3Q1OU_kQs98j0bbcBp9YZEQHsML-HWfUvVvFlHzP_w"

# Чтобы получить Refresh Token:
# 1. Открыть счет в "Финаме" https://open.finam.ru/registration
# 2. Зарегистрироваться в сервисе Comon https://www.comon.ru/
# 3. В личном кабинете Comon получить токен https://www.comon.ru/my/trade-api/tokens

class Config:
    Tinkoff = {'token': "t.EkDLxnK0MfuXiGksuurwmiogYB2UC9B60pKlvNCoqF_EKPW2Fu8jq5546AB0p-CYFV9Db-9AoOn6ETpn8nsWtQ",
               'figi_si': 'FUTSI0923000',
               'figi_rubf': 'FUTUSDRUBF00'}

    ClientIds = ('757282RDVBT')  # Торговые счёта
    AccessToken = 'CAEQ1ZACGhjrE64no9apCjdI6k+dMfQso3wM6TKzq9U='  # Торговый токен доступа
    FutJune23 = 'SiM3'
    FutSeptember23 = 'SiU3'
    FutDecember23 = 'SiZ3'
    FuturesBoard = 'FUT'
    FutUsdRubf = 'USDRUBF'
    Clearing1Start = '14:00'
    Clearing1End = '14:05'
    Clearing2Start = '18:00'
    Clearing2End = '18:05'
    
