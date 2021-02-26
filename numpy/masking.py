#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:49:05 2021

@author: whoami
"""
import numpy as np

a=np.array([3,4,6,10,24,89,45,43,46,99,100])
b=(a%3!=0)
c=(a%5==0)
d=([a%5==0,a%3==0])
e=a[a%3==0]=42
print(b)
print(c)
print('so our dth value is')
print(d)
print(a)