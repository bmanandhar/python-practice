#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:33:41 2018

@author: bijayamanandhar
"""

def luck_check(s):
    #your code here
    left, right = 0, 0
    
    if not s.isdigit():
        return False
    else:
        for i in range(len(s)//2):
            left += int(s[i])
        
        for i in range(len(s)//2, len(s)):
            right += int(s[i])
        print(left, right)
        
        if left == right:
            return True
    return False
        

print(luck_check('683179'))
print(luck_check('683000'))
print(luck_check('68300-'))