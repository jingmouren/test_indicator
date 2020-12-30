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
    M = int(N1 / 2) + 1
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


def RSV(HIGH, LOW, CLOSE, N=50):
    return (CLOSE - LLV(LOW, N)) / (HHV(HIGH, N) - LLV(LOW, N)) * 100


def KDJ(HIGH, LOW, CLOSE, N=9, M1=3, M2=3):
    _RSV = RSV(HIGH, LOW, CLOSE, N)
    K = SMA(_RSV, M1, 1)
    D = SMA(K, M2, 1)
    J = 3 * K - 2 * D
    return K, D, J


def MACD(CLOSE, SHORT=12, LONG=26, MID=9):
    DIF = EMA(CLOSE, SHORT) - EMA(CLOSE, LONG)
    DEA = EMA(DIF, MID)
    _MACD = (DIF - DEA) * 2
    return DIF, DEA, _MACD


def DMI(HIGH, LOW, CLOSE, N=14, M=6):
    MTR = SUM(MAX(MAX(HIGH - LOW, ABS(HIGH - REF(CLOSE, 1))), ABS(REF(CLOSE, 1) - LOW)), N)
    HD = HIGH - REF(HIGH, 1)
    LD = REF(LOW, 1) - LOW
    DMP = SUM(IF((HD > 0) & (HD > LD), HD, 0), N)
    DMM = SUM(IF((LD > 0) & (LD > HD), LD, 0), N)
    PDI = DMP * 100 / MTR
    MDI = DMM * 100 / MTR
    ADX = MA(ABS(MDI - PDI) / (MDI + PDI) * 100, M)
    ADXR = (ADX + REF(ADX, M)) / 2
    return PDI, MDI, ADX, ADXR


def EXPMA(CLOSE, M1=12, M2=50):
    EXP1 = EMA(CLOSE, M1)
    EXP2 = EMA(CLOSE, M2)
    return EXP1, EXP2


def TRIX(CLOSE, N=12, M=9):
    MTR = EMA(EMA(EMA(CLOSE, N), N), N)
    _TRIX = (MTR - REF(MTR, 1)) / REF(MTR, 1) * 100
    MATRIX = MA(_TRIX, M)
    return _TRIX, MATRIX


def CCI(HIGH, LOW, CLOSE, N=14):
    TYP = (HIGH + LOW + CLOSE) / 3
    _CCI = (TYP - MA(TYP, N)) * 1000 / (15 * AVEDEV(TYP, N))
    return _CCI


def ROC(CLOSE, N=12, M=6):
    _ROC = 100 * (CLOSE - REF(CLOSE, N)) / REF(CLOSE, N)
    MAROC = MA(_ROC, M)
    return _ROC, MAROC


def RSI(CLOSE, N1=6, N2=12, N3=24):
    LC = REF(CLOSE, 1)
    RSI1 = SMA(MAX(CLOSE - LC, 0), N1, 1) / SMA(ABS(CLOSE - LC), N1, 1) * 100
    RSI2 = SMA(MAX(CLOSE - LC, 0), N2, 1) / SMA(ABS(CLOSE - LC), N2, 1) * 100
    RSI3 = SMA(MAX(CLOSE - LC, 0), N3, 1) / SMA(ABS(CLOSE - LC), N3, 1) * 100
    return RSI1, RSI2, RSI3


def WR(HIGH, LOW, CLOSE, N=10, N1=6):
    WR1 = 100 * (HHV(HIGH, N) - CLOSE) / (HHV(HIGH, N) - LLV(LOW, N))
    WR2 = 100 * (HHV(HIGH, N1) - CLOSE) / (HHV(HIGH, N1) - LLV(LOW, N1))
    return WR1, WR2


def MIKE(HIGH, LOW, CLOSE, N=10):
    HLC = REF(MA((HIGH + LOW + CLOSE) / 3, N), 1)
    HV = EMA(HHV(HIGH, N), 3)
    LV = EMA(LLV(LOW, N), 3)
    STOR = EMA(2 * HV - LV, 3)
    MIDR = EMA(HLC + HV - LV, 3)
    WEKR = EMA(HLC * 2 - LV, 3)
    WEKS = EMA(HLC * 2 - HV, 3)
    MIDS = EMA(HLC - HV + LV, 3)
    STOS = EMA(2 * LV - HV, 3)
    return STOR, MIDR, WEKR, WEKS, MIDS, STOS


def BOLLINGER(CLOSE, M=20):
    BOLL = MA(CLOSE, M)
    UB = BOLL + 2 * STD(CLOSE, M)
    LB = BOLL - 2 * STD(CLOSE, M)
    return BOLL, UB, LB


def BRAR(OPEN, HIGH, LOW, CLOSE, N=26):
    BR = SUM(MAX(0, HIGH - REF(CLOSE, 1)), N) / SUM(MAX(0, REF(CLOSE, 1) - LOW), N) * 100
    AR = SUM(HIGH - OPEN, N) / SUM(OPEN - LOW, N) * 100
    return BR, AR


def CR(HIGH, LOW, N=26, M1=10, M2=20, M3=40, M4=62):
    MID = REF(HIGH + LOW, 1) / 2
    _CR = SUM(MAX(0, HIGH - MID), N) / SUM(MAX(0, MID - LOW), N) * 100
    MA1 = REF(MA(_CR, M1), M1 / 2.5 + 1)
    MA2 = REF(MA(_CR, M2), M2 / 2.5 + 1)
    MA3 = REF(MA(_CR, M3), M3 / 2.5 + 1)
    MA4 = REF(MA(_CR, M4), M4 / 2.5 + 1)
    return _CR, MA1, MA2, MA3, MA4


def VR(CLOSE, VOL, N=26, M=6):
    TH = SUM(IF(CLOSE > REF(CLOSE, 1), VOL, 0), N)
    TL = SUM(IF(CLOSE < REF(CLOSE, 1), VOL, 0), N)
    TQ = SUM(IF(CLOSE == REF(CLOSE, 1), VOL, 0), N)
    _VR = 100 * (TH * 2 + TQ) / (TL * 2 + TQ)
    MAVR = MA(_VR, M)
    return _VR, MAVR


def OBV(CLOSE, VOL, M=30):
    VA = IF(CLOSE > REF(CLOSE, 1), VOL, -VOL)
    _OBV = SUM(IF(CLOSE == REF(CLOSE, 1), 0, VA), 0)
    MAOBV = MA(_OBV, M)
    return _OBV, MAOBV


def EMV(HIGH, LOW, VOL, N=14, M=9):
    VOLUME = MA(VOL, N) / VOL
    MID = 100 * (HIGH + LOW - REF(HIGH + LOW, 1)) / (HIGH + LOW)
    _EMV = MA(MID * VOLUME * (HIGH - LOW) / MA(HIGH - LOW, N), N)
    MAEMV = MA(_EMV, M)
    return _EMV, MAEMV


def WVAD(OPEN, HIGH, LOW, CLOSE, VOL, N=24, M=6):
    _WVAD = SUM((CLOSE - OPEN) / (HIGH - LOW) * VOL, N) / 10000
    MAWVAD = MA(_WVAD, M)
    return _WVAD, MAWVAD
