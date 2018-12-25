#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:17:16 2018

@author: bijayamanandhar
"""

""" Correct """
def greatest_common_factor(x, y):
    while(y):
        x, y = y, x%y
    return x
f = greatest_common_factor(10, 400)
print(f)
