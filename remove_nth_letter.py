#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:54:14 2018

@author: bijayamanandhar
"""

def remove_nth_letter(string, n):
    
    x = list(string)
    new_str = ''
    
    for i in range(len(x)):
        if i != n:
            new_str += x[i]
    return new_str

print(remove_nth_letter('abcXdef', 3) == 'abcdef')
