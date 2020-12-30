# coding=utf-8

# Author: mathchq <mathchq@gmail.com>

from os.path import isfile

import pandas as pd

from sw.indicator import *
from gf.indicator import *
from utils.tools import download_index
from utils.tdx import *
from strategy.kdj import *

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


def cal_all_indicator(df):
    df['dpo'] = DPO(CLOSE)
    df['k'], df['d'], df['j'] = KDJ(HIGH, LOW, CLOSE)
    df['dif'], df['dea'], df['macd'] = MACD(CLOSE)
    df['pdi'], df['mdi'], df['adx'], df['adxr'] = DMI(HIGH, LOW, CLOSE)
    df['exp1'], df['exp2'] = EXPMA(CLOSE)
    df['trix'], df['ma_trix'] = TRIX(CLOSE)
    df['cci'] = CCI(HIGH, LOW, CLOSE, N=14)
    df['roc'], df['ma_roc'] = ROC(CLOSE)
    df['rsi1'], df['rsi2'], df['rsi3'] = RSI(CLOSE)
    df['wr1'], df['wr2'] = WR(HIGH, LOW, CLOSE)
    df['stor'], df['midr'], df['wekr'], df['weks'], df['mids'], df['stos'] = MIKE(HIGH, LOW, CLOSE)
    df['boll'], df['ub'], df['lb'] = BOLLINGER(CLOSE, M=20)
    df['br'], df['ar'] = BRAR(OPEN, HIGH, LOW, CLOSE)
    df['cr'], df['ma1'], df['ma2'], df['ma3'], df['ma4'] = CR(HIGH, LOW)
    df['vr'], df['ma_vr'] = VR(CLOSE, VOL)
    df['obv'], df['ma_obv'] = OBV(CLOSE, VOL)
    df['asi'] = ASI(OPEN, HIGH, LOW, CLOSE)
    df['emv'], df['ma_emv'] = EMV(HIGH, LOW, VOL, N=14, M=9)
    df['wvad'], df['ma_wavd'] = WVAD(OPEN, HIGH, LOW, CLOSE, VOL)
    df['bull_power'], df['bear_power'] = ER(HIGH, LOW, CLOSE)
    df['tii'] = TII(CLOSE)
    df['po'] = PO(CLOSE)
    df['t3'] = T3(CLOSE)


def test_kdj_strategy(df):
    df['k'], df['d'], df['j'] = KDJ(HIGH, LOW, CLOSE)
    df['k_bs_status'] = cal_bs_status(df['k'], K_BS_STATUS)
    df['d_bs_status'] = cal_bs_status(df['d'], D_BS_STATUS)
    df['j_bs_status'] = cal_bs_status(df['j'], J_BS_STATUS)
    df['cross_type'] = cross_type(df['k'], df['d'])
    df['long_short'] = ls_status(df['k'], df['d'])


if __name__ == '__main__':
    index_code = '603588'
    data_dir = 'data'
    import tushare as ts
    
    df = ts.get_k_data('603588', start='1989-01-01', autype='qfq')
    # 文件不存在，则下载相应的指数
    # if not isfile(f'{data_dir}/{index_code}.csv'):
    #     download_index(data_dir=data_dir, index=index_code)
    # df = pd.read_csv(f'{data_dir}/{index_code}.csv')
    
    # 提取开高收低，成交量
    OPEN, HIGH, CLOSE, LOW, VOL = df['open'], df['high'], df['close'], df['low'], df['volume']
    test_kdj_strategy(df)
    df.to_csv('data/603588.csv', index=False)

    # print(df['t3'])
    # sar, adl, adr, obos,
