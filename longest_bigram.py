#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 17:57:36 2018

@author: bijayamanandhar
"""

def longest_bigram(str):
    
    str_split = str.split()
    longest_bigram = ''
    
    for i in range(len(str_split)-1):
        
        x = str_split[i] + ' ' + str_split[i+1]
        
        if len(x) > len(longest_bigram):

            longest_bigram = x
    
    return longest_bigram
print(longest_bigram("One must have a mind of winter") == 'must have')

