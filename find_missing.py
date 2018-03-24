#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:22:10 2018

@author: bijayamanandhar
"""


def find_missing(seq):
    
    missing = 0
    x = seq[1] -seq[0]
    y = seq[2] -seq[1]
    
    if x > y: 
        missing = x[2] -x[1] +x[0]
    elif y > x:
        missing = 2 *x[1] -x[0]
    else:        
        for i in range(2, len(seq) -1):
            if seq[i] +x != seq[i +1]:
                missing = seq[i] +x
    
    return missing
print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]), 5)

print(find_missing([1,3,5,9,11]), 7)
