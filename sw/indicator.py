# coding=utf-8

# Author: mathchq <mathchq@gmail.com>

from utils.tdx import *


def AC(HIGH, LOW, nDay=5, mDay=34):
    """
    第二集 Accelerator Oscillator
    加速震荡指标
    :param HIGH:
    :param LOW:
    :param nDay:
    :param mDay:
    :return:
    """
    MP = (HIGH + LOW) / 2
    AO = MA(MP, nDay) - MA(MP, mDay)
    return AO - MA(AO, nDay)
    
    
def ASI(OPEN, HIGH, CLOSE, LOW):
    
    VAR1 = ABS(HIGH - REF(CLOSE, 1))
    VAR2 = ABS(LOW - REF(CLOSE, 1))
    VAR3 = ABS(HIGH - REF(LOW, 1))
    VAR4 = ABS(REF(CLOSE, 1) - REF(OPEN, 1))
    VAR5 = CLOSE - REF(CLOSE, 1)
    VAR6 = CLOSE - REF(OPEN, 1)
    VAR7 = REF(CLOSE, 1) - REF(OPEN, 1)
    X = VAR5 + 0.5 * VAR6 + VAR7
    K = MAX(VAR1, VAR2)
    R1 = VAR1 + 0.5 * VAR2 + 0.25 * VAR4
    R2 = VAR2 + 0.5 * VAR1 + 0.25 * VAR4
    R3 = VAR3 + 0.25 * VAR4
    R = IF((VAR1 >= VAR2) & (VAR1 >= VAR3), R1, IF((VAR2 > VAR1) & (VAR2 >= VAR3), R2, R3))
    SIVAL = 50 / 3 * X * K / R
    ASIVAL = SUM(SIVAL, 2)
    return ASIVAL

