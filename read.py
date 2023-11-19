from __future__ import print_function

import collections
import os
import pickle
import pandas as pd

def read():
    reuters = collections.defaultdict(list)
    for ls in os.listdir('data'):
        if ls.endswith('.pkl'):
            f = open('data/' + ls, 'rb')
            data = pickle.load(f, encoding='utf-8')
            for datum in data:
                #print('ts = {}, t = {}, h= {}'.format(datum['ts'], datum['title'], datum['href']))
                reuters["timeStamp"].append(datum['ts'])
                reuters["headline"].append(datum['title'])
                reuters["href"].append(datum['href'])
            f.close()
    pd.DataFrame(reuters).to_csv("reuters.csv")


if __name__ == '__main__':
    read()
