# coding=utf-8

# Author: mathchq <mathchq@gmail.com>

import numpy as np


def REF(series, offset):
    return series.shift(offset)


def ABS(series):
    return series.abs()


def SUM(series, num):
    return series.rolling(num if num else len(series), min_periods=1).sum()


def IF(cond, result1, result2):
    return np.where(cond, result1, result2)


def MAX(series1, series2):
    return np.maximum(series1, series2)


def HHV(series, n):
    return series.rolling(n, min_periods=1).max()


def LLV(series, n):
    return series.rolling(n, min_periods=1).min()


def MA(series, n):
    return series.rolling(n, min_periods=1).mean()


def EMA(series, n):
    return series.emw(span=n, adjust=False).mean()


def AVEDEV(series, n):
    return series.rolling(n, min_periods=1).apply(lambda x: np.fabs(x - x.mean()).mean(), raw=True)
