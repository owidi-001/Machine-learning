#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:29:06 2021

@author: whoami
"""
# rectangle
x=20
y=5
count=0
for i in range(y):
    for j in range(x):
              print('*',end='')
    print(end='\n')
    
print('end one \n')


for i in range(y):
    print('*',end='')
    for j in range(x):
        if i==0 or i==y-1:
            print('*',end='')
        elif j==x-1:
            print(end='*')
    print(end='\n')
    
print('End two \n')


for i in range(x):
    print('*'*i,end='\n')
    
print('End three \n')


print((512-282)/(47·48+5))