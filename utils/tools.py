# coding=utf-8

# Author: mathchq <mathchq@gmail.com>

import tushare as ts

from os.path import isdir, isfile
from os import makedirs


def download_index(data_dir='data', index='000300'):
    if not isdir(data_dir):
        makedirs(data_dir)
    k = ts.get_k_data(code=index, start='1989-01-01', index=True)
    k.to_csv(f'{data_dir}/{index}.csv', index=False)


if __name__ == '__main__':
    download_index()
