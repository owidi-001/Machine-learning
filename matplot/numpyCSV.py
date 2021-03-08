# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 00:57:03 2021

@author: young
"""

import numpy as np
from matplotlib import pyplot as plt,style

style.use('ggplot')

x,y=np.loadtxt('file.txt',unpack=True)
plt.plot(float(x),float(y),label='Numpy loaded',color='k')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Test numpy loads')

plt.legend()

plt.show()
