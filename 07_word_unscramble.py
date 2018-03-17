#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:47:31 2018

@author: bijayamanandhar
"""

# 07 Word Unscrambler:

def word_unscrambler(word, dictionary):
    
    anagrams = []
    s1 = sorted(list(word))
    
    for elm in dictionary:
        s2 = sorted(list(elm))
        if s1 == s2:
            anagrams.append(elm)
    
    return anagrams
print(word_unscrambler('cat', ['tac']))