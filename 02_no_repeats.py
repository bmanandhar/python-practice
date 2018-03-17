#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:27:34 2018

@author: bijayamanandhar
"""

# 02 No Repeats Years

def no_repeats(year_start, year_end):
    
    years = []
    
    if year_start > year_end: return False
    
    if year_start == year_end:
        
        if len(str(year_start)) == len(set(str(year_start))):
            years.append(year_start)    
        
    for year in range(year_start, year_end):
        
        if len(str(year)) == len(set(str(year))):
            years.append(year)
            
    return years

print("xxx == Test for no_repats Years === xxx")
print()
print(no_repeats(1234, 1234))
print(no_repeats(1999, 1990))
print(no_repeats(1980, 1990))
print()
