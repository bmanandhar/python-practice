#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:54:03 2018

@author: bijayamanandhar
"""

"""while loop"""

def disemvowel(text):
    x = ''
    i = 0
    while i < len(text):
        
        if text[i] not in 'aAeEiIoOuU':
            x += text[i]
            
        i += 1
    return x
print(disemvowel('America'))

""" for loop"""

def disemvowel(text):
    x = ''
    for i in text:
        if i not in 'aAeEiIoOuU':
            x += i
    return x
print(disemvowel('United States of America'))