#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 16:51:03 2018

@author: bijayamanandhar
"""

def most_frequent(arr):
    most_freq_elem = 0
    frequency = 1
    
    x = list(set(arr))
    
    i = 0
    while i < len(x):
        y = arr.count(x[i])
        if y > frequency:
            frequency = y
            most_freq_elem = x[i]
        i += 1
    return "Most Frequent Element is ", most_freq_elem, "Frequency: ", frequency

print(most_frequent([1, 2, 3, 1, 1, 4, 4]))