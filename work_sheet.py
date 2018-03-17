#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:54:37 2018

@author: bijayamanandhar
"""

x = ['a', 'b', 'c', 'd']
for i, x in enumerate(x):
    print(i, x)


for i in range(len(x)):
        print(i, x, 9)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for fruit in sorted(set(basket)):
    print(fruit )

