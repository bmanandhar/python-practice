#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:09:39 2018

@author: bijayamanandhar
"""

        
""" third greatest number """
def third(n):
    num = 0
    new = []

    x = 0
    while x < 3: 

        for i in range(len(n)):
            if n[i] > num:
                num = n[i] 
                                           
        new.append(n[i])
        del n[i]
        x += 1
        
    return new[2]
print(third([5, 6, 10, 11]), num)   
    