#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:39:01 2018

@author: bijayamanandhar
"""

def nth_prime(n):
    prime_num = 0
    
    i = 2
    while True:
        if is_prime(i):
            prime_num += 1
            if is_prime == n:
                return i
        i += 1
print(nth_prime(10))