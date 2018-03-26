#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:54:14 2018

@author: bijayamanandhar
"""

def remove_nth_letter(string, n):
    
    new_str = ''
    
    for i in range(len(string)):
        if i != n:
            new_str += string[i]
    return new_str

print(remove_nth_letter('abcXdef', 3) == 'abcdef')


#Function 2:

def remove_nth_letter(string, n):
    
    return string[:n]+string[n+1:]

print(remove_nth_letter('abcXdef', 3))
