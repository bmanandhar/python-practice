#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:27:34 2018

@author: bijayamanandhar
"""

# 02 No Repeats Years

# no_repeats using a helper function :

def not_duplicate(arr):
    
    chk_list = []
    
    for i in arr:
        if i not in chk_list:
            chk_list.append(i)
            
    return len(chk_list) == len(arr)

#main function

def no_repeats(start, end):
    
    no_repeats = []
    
    for i in range(start, end + 1):
        split_into_list = list(str(i))
        if not_duplicate(split_into_list):
            no_repeats.append(i)
            
    return no_repeats
        
print(no_repeats(1987, 2018) == [1987, 2013, 2014, 2015, 2016, 2017, 2018])
# should return:
# [1987, 2013, 2014, 2015, 2016, 2017, 2018]

#----------------------------------

#no_repeats using set and list

def no_repeats(year_start, year_end): #main function

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
