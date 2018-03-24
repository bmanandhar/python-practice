#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:12:11 2018

@author: bijayamanandhar
"""

def third_num(num):
    
    i, ii, iii = 0, 0, 0
    for x in range(len(num)):
        if i == 0 or num[x] > i:
            iii, ii, i = ii, i, num[x]
            
        elif ii == 0 or num[x] > ii:
            iii, ii = ii, num[x]
        
        elif iii == 0 or num[x] > iii:
            iii = num[x]
        
    return iii
print(third_num([4,8,5,7])) 