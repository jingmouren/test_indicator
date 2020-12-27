# coding=utf-8

# Author: mathchq <mathchq@gmail.com>

from os.path import isfile

import pandas as pd

from sw.indicator import *
from gf.indicator import *
from utils.tools import download_index
from utils.tdx import *
"""
dataframe的结构

        date     open    close     high     low      volume      code
0 2005-04-08   984.66  1003.45  1003.70  979.53  14762500.0  sh000300
1 2005-04-11  1003.88   995.42  1008.73  992.77  15936100.0  sh000300
2 2005-04-12   993.71   978.70   993.71  978.20  10226200.0  sh000300
3 2005-04-13   987.95  1000.90  1006.50  987.95  16071700.0  sh000300
4 2005-04-14  1004.64   986.97  1006.42  985.58  12945700.0  sh000300
"""


def test_ac(df):
    import mplfinance as mpf
    
    # ac = AC(HIGH, LOW)
    # df.plot(subplots=True, figsize=(16, 9))
    
    ma5_plot = mpf.make_addplot(MA(CLOSE, 5), type='line')
    ma10_plot = mpf.make_addplot(MA(CLOSE, 10), type='line')
    
    mpf.plot(df, type='candle', addplot=[ma5_plot, ma10_plot], volume=True)
    mpf.show()


if __name__ == '__main__':
    index_code = '000300'
    data_dir = 'data'
    
    # 文件不存在，则下载相应的指数
    if not isfile(f'{data_dir}/{index_code}.csv'):
        download_index(data_dir=data_dir, index=index_code)
    df = pd.read_csv(f'{data_dir}/{index_code}.csv', parse_dates=['date'], infer_datetime_format='%Y-%m-%d')
    # 提取开高收低，成交量
    OPEN, HIGH, CLOSE, LOW, VOL = df['open'], df['high'], df['close'], df['low'], df['volume']
    
    df['dpo'] = DPO(CLOSE)
    df['bull_power'], df['bear_power'] = ER(HIGH, LOW, CLOSE)
    df['tii'] = TII(CLOSE)
    df['po'] = PO(CLOSE)
    df['t3'] = T3(CLOSE)
    
    print(df['t3'])
