#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : test.py
@Time    : 5/7/2020 3:01 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

from icd9 import ICD9
import numpy as np
import pandas as pd
import string
tree = ICD9('codes.json')
toplevelnodes = tree.children
toplevelcodes = [node.code for node in toplevelnodes]

#print(tree.find('E001.0').parent.descr)
Category_list = []
Category_code_list = []
ICD_9 = pd.read_csv('descriptions.csv',encoding='latin-1')
#print(ICD_9.info())
#print(ICD_9["icd9code"])
for index,code in ICD_9.iterrows():
    _ = code['icd9code']
    try:
        Category = tree.find(_).parent.descr
        Category_code = tree.find(_).parent.code
        #print(Category,Category_code)
    except:
        Category = 'None'
        Category_code = 'None'
    Category_list.append(Category)
    Category_code_list.append(Category_code)
    #print(Category_code_list[:5])
ICD_9['Category']  = pd.Series(Category_list,dtype='str')
ICD_9['Category_code']  = pd.Series(Category_code_list,dtype='str')
ICD_9.to_csv('ICD_Code_test.csv')
ICD_9 = ICD_9.reindex(columns=['Category_code','Category','icd9code','long_description','short_description'])
ICD_9.to_csv('ICD_Code.csv',index=False)