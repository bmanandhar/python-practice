#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:24:53 2018

@author: bijayamanandhar
"""


""" Euler on fibonacci, sum of even terms """

def prime_func(x):
    """ empty list """
    primes = []
    
    """ recursive """
    for x in range(2, x):        
        prime = True
        
        """ check if prime """
        for i in range(2, x):
            if x % i == 0:
                prime = False
        
        """ add to list if prime """
        if prime:
           primes.append(x)
    return primes
print(prime_func(100))