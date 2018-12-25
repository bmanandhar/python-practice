#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:57:35 2018

@author: bijayamanandhar
"""
"""XXXXXXXXXX To Be Corrected XXXXXXXXXX"""
def palindrome(string):
    i = 0
    while i < len(string):
        if string[i] != string[(len(string) - 1) - i]:
            return False
        i += 1
    return True

def longest_palindrome(string):
    best_palindrome = ''
    idx1 = 0
    while idx1 < len(string):
        length = 1
        while (idx1 + length) <= len(string):
            substring = string.slice(idx1, length)
            if palindrome(substring) == '' and (best_palindrome) == '':
                if len(substring) > len(best_palindrome):
                    best_palindrome = substring
            length += 1
        idx1 += 1
    return best_palindrome
print(longest_palindrome('abcxcbadcd'))
