#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:37:06 2018

@author: bijayamanandhar
"""

# this code has been written in Python

def crazy_sum(x):
    total = 0

    for i in range(len(x)):
        total += x[i]*i
    return total
print(crazy_sum([2,3,5,2]))
print(crazy_sum([2]) == 0) # (2*0)
print(crazy_sum([2, 3]) == 3) # (2*0) + (3*1)
print(crazy_sum([2, 3, 5]) == 13) # (2*0) + (3*1) + (5*2)
print(crazy_sum([2, 3, 5, 2]) == 19) # (2*0) + (3*1) + (5*2) + (2*3)