import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from flask import send_file
import datetime
import json

ticker = 'SBER'
start_date = '2020-01-01'


class Stocks():

    def __init__(self, ticker, start_date):
        req = requests.get(f"http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{ticker}.json?&from={start_date}&iss.meta=off")
        self.data = pd.DataFrame.from_records(req.json()['history']['data'])
        self.columns = req.json()['history']['columns']



    def sma(self):
        self.data['SMA(5)'] = self.data.GLD.rolling(5).mean()

    def plot(self):
        fig, ax = plt.subplots()
        time, val = self.data['1'], self.data['11']
        plt.plot(time, val)
        img = BytesIO()
        fig.savefig(img)
        img.seek(0)
        return send_file(img, mimetype='image/png')

    # def get_data(self, ticker, start_date):
    #     req = requests.get(
    #         f"http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{ticker}.json?&from={start_date}&iss.meta=off")
    #     return pd.DataFrame.from_records(req.json()['history']['data'])
    #     self.columns = req.json()['history']['columns']



print(Stocks(ticker,start_date).data)
print(Stocks(ticker,start_date).columns)
