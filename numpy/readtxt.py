#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:02:00 2021

@author: whoami
"""

import numpy as np
from matplotlib import pyplot as plt,style
style.use('ggplot')

readFile=np.genfromtxt('data.csv',delimiter=',')
# plt.plot(readFile,marker='o',color='k',label='random')
plt.plot([1,2,3,4,5],[4,5,6,7,8],marker='o',color='k',label='random')

plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.legend()

plt.show()
