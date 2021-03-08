#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 12:21:38 2021

@author: whoami
"""

import tensorflow as tf

A=tf.constant([[3,4],[7,4]])
B=tf.constant([[6,5],10,3])
AB_concate=tf.concat(values=[A,B], axis=1)
print(A)