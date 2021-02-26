#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 22:00:32 2021

@author: whoami
"""

import numpy as np
max=eval(input('Enter max values:\n'))

is_prime = np.ones((max,), dtype=bool)

# Cross out 0 and 1 which are not primes:
is_prime[:2] = 0

# cross out its higher multiples (sieve of Eratosthenes):
nmax = int(np.sqrt(len(is_prime)))
for i in range(2, nmax):
    is_prime[2*i::i] = False

a=np.nonzero(is_prime)
print(np.nonzero(is_prime))

                    
                    