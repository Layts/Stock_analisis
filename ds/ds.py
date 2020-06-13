import pandas as pd
import matplotlib.pyplot as plt
import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPY&apikey=R#PE1#E7KZ#66X#N&datatype=csv&outputsize=full'  # адрес запроса для получения данных

r = requests.get(url)  # сделаем запрос к Alpha Vantage
content = r.content.decode('UTF-8')
with open('SPY.csv', 'w') as f:
    f.write(content)

data = pd.read_csv('SPY.csv', index_col='timestamp', parse_dates=True)  # прочитаем файл
data['close'].plot(legend=True)  # построим график

plt.show()