#!/usr/bin/python
# -*- coding: windows-1250 -*-

import pandas as pd
import random
import numpy as np

doba = 100

def daily_return():
    return np.random.normal(0.0038, 0.0098)


df = pd.DataFrame(index=range(1, doba + 1))

#df['Daily return'] = daily_return()
df['D_return'] = np.random.normal(0.0038, 0.0098, len(df))

print(df)
