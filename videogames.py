#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:36:17 2021

@author: whoami
"""
import pandas as pd

df=pd.read_csv('vgsales.csv')

print(df.shape)
print(df.describe)
print(df.values)