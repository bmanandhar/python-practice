#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:07:37 2018

@author: bijayamanandhar
"""


""" dasherize number """

def dash(n):
    x = str(n)
    result = ""
    
    for i in range(len(x)):
        digit = int(x[i])
        
        if i > 0:
            pre_digit = int(x[i-1])
            
            if pre_digit % 2 == 1\
            or digit % 2 == 1:            
                result += "-"
        result += x[i]

    return result
print(dash(3370))