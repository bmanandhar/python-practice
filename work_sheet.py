#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:57:41 2018

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


a ='fcvh89hhd'
b = set(a)
print(b)
c = {0,1,2,3,4,5,6,7,8}
d = zip(b, c)
e_dict = dict(d)
print(e_dict)

{'8': 3, 'h': 4, '9': 0, 'f': 1, 'c': 6, 'd': 2, 'v': 5}


{'8': 3, 'h': 4, '9': 0, 'f': 1, 'c': 6, 'd': 2, 'v': 5}

