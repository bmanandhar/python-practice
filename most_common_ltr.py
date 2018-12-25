#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:05:33 2018

@author: bijayamanandhar
"""


""" most common letter """
def most_common_ltr(x):
    
    mcl = ""
    cnt = 0
    
    for i in range(len(x)):
        ltr = x[i]
        c = 0
        
        for j in range(len(x)):
            if x[j] == ltr:
                c += 1
        if mcl == "" or c > cnt:
            mcl = ltr
            cnt = c
    return [mcl, cnt]
print(most_common_ltr("abcdaca"))
