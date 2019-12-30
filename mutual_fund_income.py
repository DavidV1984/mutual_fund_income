#!/usr/bin/python
# -*- coding: windows-1250 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# doba v dnevih (252 dni = 1 leto)
doba = 1000

# upravljavska provizija na letni osnovi
mngt_fee = 0.012


def dnevni_donos():
    # return random.gauss(0.00038, 0.0098)
    return (np.random.choice(a=[np.random.normal(0.00038, 0.0098), -0.03], p=[0.99, 0.01]))


def fund():
    # ustvarimo dataframe
    df = pd.DataFrame()

    # ustvarimo naključna vplačila
    df['Inf'] = np.random.choice(a=[0, 1000, 2500, 5000, 10000, 15000, 25000, 50000, 100000],
                                 p=[0.5, 0.2, 0.1, 0.05, 0.04, 0.03, 0.03, 0.03, 0.02],
                                 size=doba)

    # AUM brez donosa (skupna vplačila)
    df['Inf_sum'] = df['Inf'].cumsum()

    # AUM z bruto dnevnim donosom + dnevni donos
    AUM_d = []
    d_return = []
    aumd = 0
    for row in df['Inf']:
        ddonos = dnevni_donos()
        izr = round(aumd * (1 + ddonos) + row, 2)
        aumd = izr
        AUM_d.append(izr)
        d_return.append(ddonos)
    df['AUM_d_b'] = AUM_d
    df['D_return'] = d_return
    df['Sum_return'] = df['D_return'].cumsum()
    df['12M_return'] = df['Sum_return'].pct_change(252)
    df['Mngt_Fee'] = df['AUM_d_b'] * mngt_fee / 252

    print(df.tail(15))

    plt.plot(df.index, df['Sum_return'])
    plt.show()


fund()
