#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:29:39 2018

@author: bijayamanandhar
"""

# 03 Letter Count String

# Write a function, `letter_count(str)` that takes a string and
# returns a hash mapping each letter to its frequency. Do not include
# spaces.
#
# Difficulty: 1/5
def letter_count(str):
    dict = {}
    
    for char in str:
        if char != ' ':
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
         
    return dict
print(letter_count('abcadec'))


def letter_count(str):
    h = {}
    
    for char in str:
        h[char] = h.get(char, 0) + 1
            
    return h

print("Tests for letter counts in string")
print(letter_count('hello') == {'h': 1, 'e': 1, 'l': 2, 'o': 1})
print(letter_count("cats are fun") == {'a': 2, 'c': 1,\
      'e': 1,'f': 1, 'n': 1, 's': 1, 'r': 1, 'u': 1, 't': 1})
print("=========xxx=============")

