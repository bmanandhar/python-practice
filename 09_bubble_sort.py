#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:51:08 2018

@author: bijayamanandhar
"""

# 09 Bubble Sort:

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) -1 -i):
            if arr[j] > arr[j +1]:
                arr[j], arr[j +1] = arr[j +1], arr[j]                
    return arr

print(bubble_sort([2, 5, 1, 3, 6, 4]))
print(bubble_sort(['f', 'e', 'a', 'c', 'd', 'b']))
