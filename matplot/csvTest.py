# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 00:31:51 2021

@author: young
"""
from matplotlib import pyplot as plt,style
import csv

style.use('ggplot')
x=list()
y=list()

#open csv file for reading
#with open('sample3.csv','r') as csvfile:
#    plots=csv.reader(csvfile)
#    for rows in range(1,len(plots)):
#       x.append(int(rows[0]))
#        y.append(int(rows[1]))
        
with open('sample3.csv','r') as csvfile:
    plots=csv.reader(csvfile)
    for rows in plots:
        x.append(int(rows[0]))
        y.append(int(rows[1]))
        
        
#plot the x an y graphs
plt.plot(x,y, label='Read from csv',color='g')

plt.xlabel('Game Number') 
plt.ylabel('Game value')
plt.title('CSV Random plot')

plt.legend()
plt.show()       