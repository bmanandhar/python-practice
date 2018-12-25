#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:36:38 2018

@author: bijayamanandhar
"""

def is_prime(number):
    
    """ only number > 1 
        can be prime """  
    if number <= 1:        
        return False

    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
        
    return True
print(is_prime(2))