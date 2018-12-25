#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:48:21 2018

@author: bijayamanandhar
"""

def meters(x):
    #your code here
    unit = ''
    
    if x < 10**3: 
        unit = ''
        
    elif x < 10**6:
        x = x /(10**3)
        unit = 'k'
        
    elif x < 10**9:
        x = x /(10**6)
        unit = 'M'
        
    elif x < 10**12:
        x = x/(10**9)
        unit = 'G'
        
    elif x < 10**15:
        x = x/(10**12)
        unit = 'T'
        
    elif x < 10**18:
        x = x/(10**15)
        unit = 'P'
        
    elif x < 10**21:
        x = x/(10**18)
        unit = 'E'
        
    elif x < 10**24:
        x = x/(10**21)
        unit = 'Z'

    else: 
        x = x/(10**24)
        unit = 'Y'
    
    if x % 1 == 0:
        x = int(x)
    
    return "{}{}{}".format(x, unit, 'm') 
    
    
print((1), "1m")
print(meters(1000), "1km")
print(meters(12300000), "12.3Mm")   
print(meters(12300000000), "12.3Gm") 