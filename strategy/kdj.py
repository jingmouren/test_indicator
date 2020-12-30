# coding=utf-8

# Author: mathchq <mathchq@gmail.com>

import pandas as pd
import numpy as np

OVER_SELL = 'oversell'  # 超卖
OVER_BUY = 'overbuy'  # 超买
LINGERING = 'lingering'  # 徘徊
LONG = 'long'
SHORT = 'short'
GOLDEN = 'golden'
DEATH = 'death'
NAN = 'nan'

K_BS_STATUS = {pd.Interval(left=-np.inf, right=20): OVER_SELL, pd.Interval(20, 80): LINGERING,
               pd.Interval(left=80, right=np.inf): OVER_BUY}

D_BS_STATUS = K_BS_STATUS

J_BS_STATUS = {pd.Interval(left=-np.inf, right=0): OVER_SELL, pd.Interval(0, 100): LINGERING,
               pd.Interval(left=100, right=np.inf): OVER_BUY}

CROSS_DICT = {1: GOLDEN, -1: DEATH, 0: NAN}

LONG_SHORT_DICT = {1: LONG, -1: SHORT, 0: NAN}


def cal_bs_status(indicator, bs_status):
    return indicator.apply(lambda x: [bs_status[_] for _ in bs_status.keys() if x in _][0])


def _golden_cross(k, d, k_center=20, k_offset=2):
    is_k_near_center = k.apply(lambda x: x in pd.Interval(k_center - k_offset, k_center + k_offset))
    return is_k_near_center & (k > d) & (k.shift(1) <= d.shift(1))


def _death_cross(k, d, k_center=80, k_offset=2):
    is_k_near_center = k.apply(lambda x: x in pd.Interval(k_center - k_offset, k_center + k_offset))
    return is_k_near_center & (k < d) & (k.shift(1) >= d.shift(1))


def cross_type(k, d):
    cross = pd.DataFrame()
    cross['death'] = np.where(_death_cross(k, d), -1, 0)
    cross['golden'] = np.where(_golden_cross(k, d), 1, 0)
    return cross.sum(axis=1).apply(lambda x: CROSS_DICT[x])


def _long_status(k, d, threshold=50):
    return (k >= threshold) & (d >= threshold)


def _short_status(k, d, threshold=50):
    return (k < threshold) & (d < threshold)


def ls_status(k, d):
    ls = pd.DataFrame()
    ls['long'] = np.where(_long_status(k, d), -1, 0)
    ls['short'] = np.where(_short_status(k, d), 1, 0)
    return ls.sum(axis=1).apply(lambda x: LONG_SHORT_DICT[x])
