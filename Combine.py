#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : Combine.py
@Time    : 5/25/2020 2:51 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

import pandas as pd
import numpy as np
import os

pd.set_option("display.max_rows", None, "display.max_columns", None)

result =[]

for folder in os.listdir('data/'):
    if 'city' in folder:
        df = pd.read_csv('data/' + folder,index_col=0)
        try:
            current = current.add(df, fill_value=0)
        except:
            current = df
        result = current

result.to_csv('Tweet_city.csv')

for folder in os.listdir('data/'):
    if 'country' in folder:
        df = pd.read_csv('data/' + folder,index_col=0)
        try:
            current = current.add(df, fill_value=0)
        except:
            current = df
        result = current

result.to_csv('Tweet_Country.csv')
