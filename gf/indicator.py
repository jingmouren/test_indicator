# coding=utf-8

# Author: mathchq <mathchq@gmail.com>

from utils.tdx import *


def DPO(CLOSE, N=20):
    return CLOSE - REF(MA(CLOSE, N), N / 2 + 1)
