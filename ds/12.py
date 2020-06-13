import requests
import pandas as pd
import json
import datetime

ticker = 'SBER'
start_date = '2020-01-01'
end_date = datetime.datetime.now()
def stocks(ticker,start_date, end_date):
    BS = requests.get(f"http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{ticker}.json?iss.json=extended&from={start_date}&till={end_date}&iss.meta=off")
    data = pd.DataFrame.from_dict(BS.json()[1])
    print(data)

stocks(ticker,start_date,end_date)


