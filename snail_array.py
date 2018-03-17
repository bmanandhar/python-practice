#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 21:36:53 2018

@author: bijayamanandhar
"""

def snail(array):
    result = [];

    if array and array[0]: size = len(array);
    for n in range((size+ 1) // 2):

        """ go right """
        for i in range(n, size- n):
            result.append(array[n][i]);
        """ go left """
        for j in range(n+ 1, size- n):
            result.append(array[j][- 1- n]);
        """ go down """
        for i in range(n+ 2, size- n+ 1):
            result.append(array[- 1- n][-i]);
        """ go up """
        for j in range(n+ 2, size- n):
            result.append(array[-j][n]);

    return result;

a = [['a', 'b', 'c'],
     ['h', 'i', 'd'],
     ['g', 'f', 'e']]

b =[[ 1,  2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7]]

c = [[1, 2, 3, 4, 5],
     [16,17,18,19,6],
     [15,24,25,20,7],
     [14,23,22,21,8],
     [13,12,11,10,9]]

print('a===>')
print(snail(a))
print('b===>>')
print(snail(b))
print('c===>>>')
print(snail(c))