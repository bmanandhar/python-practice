#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:18:34 2018

@author: bijayamanandhar
"""

def nearest_larger(arr, idx):

    diff = 1

    for i in range(len(arr) -1):
        left, right = idx - diff, idx + diff

        if left >= 0 and arr[left] > arr[idx]:
            return left

        elif right < len(arr) and arr[right] > arr[idx]:
            return right

        diff += 1

print("Tests for nearest larger int in arr")
print(nearest_larger([2,3,4,3], 2) == None)
print(nearest_larger([2,8,4,3], 2) == 1)
print(nearest_larger([2,6,4,8], 2) == 1)
print(nearest_larger([2,6,4,6], 2) == 1)
print(nearest_larger([8,2,4,3], 2) == 0)
print(nearest_larger([2,4,3,8], 1))
print(nearest_larger([2, 6, 4, 8], 3) == None)
print(nearest_larger([2, 6, 9, 4, 8], 3) == 2)
print("==  ==  =  ===  =  =  =  === = ===")
