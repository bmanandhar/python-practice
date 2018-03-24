#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:54:03 2018

@author: bijayamanandhar
"""

def disemvowel(text):
    x = ''
    i = 0
    while i < len(text):
        
        if text[i] not in 'aAeEiIoOuU':
            x += text[i]
            
        i += 1
    return x
print(disemvowel('America'))