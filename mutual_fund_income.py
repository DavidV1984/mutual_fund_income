#!/usr/bin/python
# -*- coding: windows-1250 -*-

import pandas as pd
import numpy as np

# doba v dnevih (252 dni = 1 leto)
doba = 252

# upravljavska provizija na letni osnovi
mngt_fee = 0.0012

# ustvarimo dataframe z indeksom
df = pd.DataFrame(index=range(1, doba + 1))

# ustvarimo vplačila
df['R_inflow'] = np.random.choice(a=[500, 1000, 2500, 5000, 10000, 15000, 25000, 50000, 100000], size=len(df))

# dodamo random dnevne donose - podatki menda za S&P 500 (normalna distribucija)
df['D_return'] = np.random.normal(0.0038, 0.0098, len(df))

print(df)
