#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:22:25 2018

@author: bijayamanandhar
"""

def twoLowest(num):
    
    if num[0] < num[1]:
        n1, n2 = num[0], num[1]
    else: n1, n2 = num[1], num[0]
    
    for i in range(2, len(num)):
        
        if num[i] < n1: n2, n1 = n1, num[i]
        elif num[i] < n2: n2 = num[i]
        
    num = n1 + n2
    return num
    
print(twoLowest([10, 11, -3, 3, 15]) == 0)
print(twoLowest([19, 1, 2, 9, 24]) == 3)
print(twoLowest([10, 40, 20, 60, 50]) == 30)
print(twoLowest([511, 6, 675, 599, 500]) == 506)
print(twoLowest([11, 6, -2, 5, -2]) == -4)    