#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 10:07:07 2018

@author: bijayamanandhar
"""

def ordered_word(str):

    letter = list(str)
    for i in range(len(letter)):

        if letter[i +1] >= letter[i]:
           return True
        else:
            return False
print(ordered_word("amz"))
print(ordered_word("zma"))
print(ordered_word("caacc"))