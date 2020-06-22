import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from aiohttp import web
import datetime
import json

ticker = 'SBER'
start_date = '2020-01-01'


class Stocks:

    def __init__(self, ticker, start_date):
        req = requests.get(f"http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{ticker}.json?&from={start_date}&iss.meta=off")
        stock_data = pd.DataFrame.from_records(req.json()['history']['data'])
        stock_data.columns = req.json()['history']['columns']
        self.data = stock_data
        self.columns = req.json()['history']['columns']

    def sma50(self):
        """
        Скользящая средняя за 50 дней
        """
        self.data['SMA(50)'] = self.data.GLD.rolling(50).mean()

    def plot(self):
        """
        Построение графика по заданным данным
        """
        fig, ax = plt.subplots()
        time, val = self.data['TRADEDATE'], self.data['CLOSE']
        plt.plot(time, val)
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        image = img.getvalue()
        return image

    # def get_data(self, ticker, start_date):
    #     req = requests.get(
    #         f"http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{ticker}.json?&from={start_date}&iss.meta=off")
    #     return pd.DataFrame.from_records(req.json()['history']['data'])
    #     self.columns = req.json()['history']['columns']

print(Stocks(ticker,start_date).columns)
