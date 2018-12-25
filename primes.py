#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:04:33 2018

@author: bijayamanandhar
"""

def primes(n):
    if n < 2: return False
    
    primes = []    
    for x in range(2, n+1):
        prime = True
        for y in range(2, x):
            if x % y == 0:
                prime = False
                break            
        if prime:
            primes.append(x)

    return primes
print(primes(100))
