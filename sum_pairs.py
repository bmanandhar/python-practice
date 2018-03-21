#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:21:00 2018

@author: bijayamanandhar
"""

def sum_pairs(ints, s):
    idx = None
    num1, num2 = None, None
    final = []
	
    for i in range(len(ints)): 
        for j in range(i +1, len(ints)):
            if ints[i] +ints[j] == s:
                
                if idx == None:
                    num1, num2 = ints[i], ints[j]
                    idx = j
                
                elif idx > j:
                    idx = j
                    num1, num2 = ints[i], ints[j]
                    final.append(num1)
                    final.append(num2)
        
    return final

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]
print(sum_pairs(l1, 8), [1, 7])
print(sum_pairs(l2, -6), [0, -6]) 
print(sum_pairs(l3, -7), [])
print(sum_pairs(l4, 2), [1, 1])
print(sum_pairs(l5, 10), [3, 7])
print(sum_pairs(l6, 8), [4, 4])
print(sum_pairs(l7, 0), [0, 0])
print(sum_pairs(l8, 10), [13, -3])