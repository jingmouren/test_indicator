# coding=utf-8

# Author: mathchq <mathchq@gmail.com>

from utils.tdx import *


def DPO(CLOSE, N=20):
    return CLOSE - REF(MA(CLOSE, N), N / 2 + 1)


def ER(HIGH, LOW, CLOSE, N=20):
    BullPower = HIGH - EMA(CLOSE, N)
    BearPower = LOW - EMA(CLOSE, N)
    return BullPower, BearPower


def TII(CLOSE, N1=40, N2=9):
    N1 = 40
    M = int(N1 / 2) + 1
    N2 = 9
    CLOSE_MA = MA(CLOSE, N1)
    DEV = CLOSE - CLOSE_MA
    DEVPOS = IF(DEV > 0, DEV, 0)
    DEVNEG = IF(DEV < 0, -DEV, 0)
    SUMPOS = SUM(DEVPOS, M)
    SUMNEG = SUM(DEVNEG, M)
    _TII = 100 * SUMPOS / (SUMPOS + SUMNEG)
    return EMA(_TII, N2)


def PO(CLOSE, short=9, long=26):
    EMA_SHORT = EMA(CLOSE, short)
    EMA_LONG = EMA(CLOSE, long)
    return (EMA_SHORT - EMA_LONG) / EMA_LONG * 100


def MADisplaced(CLOSE, M=10, N=20):
    MA_CLOSE = MA(CLOSE, N)
    return REF(MA_CLOSE, M)


def T3(CLOSE, N=20, VA=0.5):
    T1 = EMA(CLOSE, N) * (1 + VA) - EMA(EMA(CLOSE, N), N) * VA
    T2 = EMA(T1, N) * (1 + VA) - EMA(EMA(T1, N), N) * VA
    return EMA(T2, N) * (1 + VA) - EMA(EMA(T2, N), N) * VA
