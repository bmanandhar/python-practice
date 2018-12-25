#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 21:28:08 2018

@author: bijayamanandhar
"""

def wordplay(str1, str2):
        
    indices = []
    for i in range(len(str2)):
        
        if str2[i] in str1:
            indices.append(str1.index(str2[i]))    
        else:
            return False
    
    return indices

print(wordplay('substandard', 'bad') == [2, 5, 7])
print(wordplay('shadowless', 'dashes') == [3, 2, 0, 1, 7, 0])
print(wordplay('cartoon', 'lineograph') == False)