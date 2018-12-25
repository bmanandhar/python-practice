#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:51:24 2018

@author: bijayamanandhar
"""

def make_readable(s):
    # Do something
    t, h, m = [], 0, 0 
    
    while s >= 60:
        m += 1
        s -= 60
    
    while m >= 60:
        h += 1
        m -= 60
        
    t.append(str(h))
    t.append(str(m))
    t.append(str(s))
    
    for i in range(3):
        if len(t[i]) > 2:
            return "HH exceeds 99"
        elif len(t[i]) < 2:
            t[i] = '0' +t[i]   
            
    return "{}:{}:{}".format(t[0], t[1], t[2])
print(make_readable(39909))