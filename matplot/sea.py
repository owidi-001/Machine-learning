#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:59:31 2021

@author: whoami
"""

from matplotlib import pyplot as plt
import seaborn as sns

tips=sns.load_dataset('tips')
sns.set_style('whitegrid')
g=sns.lmplot(x='tip',y='total_bill',data='tips',aspect=2)
g=(g.set_axis_labels('Tip','Total bill(USD')).set(xlim=(0,100),ylim=(0,100))
plt.title('Title')
plt.show(g)