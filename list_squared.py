#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:03:16 2018

@author: bijayamanandhar
"""


def list_squared(m, n):
    # your code    
    
    final = []
        
    if m == 1:
        final.append([1, 1])          
    else:
        num = m    
        squared_list(num)
        final += squared_list(num)
       
    for i in range(m +1, n +1):
        num = i
        squared_list(num)
        final += squared_list(num)
        
    return final
    
def squared_list(num):
    import math

    array, arrays = [], [] 
    x = 1+ num*num
    
    for i in range(2, num//2+ 1):
        if num % i == 0:
            x += i*i
    if math.sqrt(x)% 1 == 0: 

        array.append(num)
        array.append(x)
        arrays.append(array)
                    
    return arrays
    
print(list_squared(1, 42) == [[1, 1], [42, 2500]])

print(list_squared(42, 250) == [[42, 2500], [246, 84100]])
print(list_squared(250, 500) == [[287, 84100]])