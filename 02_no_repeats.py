#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:27:34 2018

@author: bijayamanandhar
"""

# 02 No Repeats Years

# no_repeats using a helper function :

def dup(num_list):
    
    counter = 0
    chk_list = []
    for i in num_list:
        if i not in chk_list:
            chk_list.append(i)
        else:
            counter += 1
    return len(chk_list) == len(num_list)
        
def no_repeats(start, end):
    no_repeats = []
    
    for i in range(start, end + 1):
        year_list = list(str(i))
        if dup(year_list):
            no_repeats.append(i)
    return no_repeats

print(no_repeats(1987, 2018))

#----------------------------------

#no_repeats using set and list
def no_repeats(year_start, year_end):

    years = []

    if year_start > year_end: return False

    if year_start == year_end:

        if len(str(year_start)) == len(set(str(year_start))):
            years.append(year_start)

    for year in range(year_start, year_end + 1):

        if len(str(year)) == len(set(str(year))):
            years.append(year)

    return years

print("xxx == Test for no_repats Years === xxx")
print()
print(no_repeats(1234, 1234))
print(no_repeats(1999, 1990))
print(no_repeats(1980, 1987))
print()
