#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:49:44 2018

@author: bijayamanandhar
"""

# 08 Rectangular Intersection:

def rec_intersection(rect1, rect2):

    x_min = max(rect1[0][0], rect2[0][0])
    x_max = min(rect1[1][0], rect2[1][0])

    y_min = max(rect1[0][1], rect2[0][1]) 
    y_max = min(rect1[1][1], rect2[1][1])
    
    if x_min > x_max:
        return None
    
    else: return [[x_min, y_min], [x_max, y_max]] 

    
print("Test for rec intersection")
print(rec_intersection([[0, 0], [2, 1]], [[1, 0], [3, 1]]) == [[1, 0], [2, 1]])
print(rec_intersection([[1, 1], [2, 2]], [[0, 0], [5, 5]]) == [[1, 1], [2, 2]])
print(rec_intersection([[1, 1], [2, 2]], [[4, 4], [5, 5]]) == None)
print(rec_intersection([[1, 1], [5, 4]], [[2, 2], [3, 5]]) == [[2, 2], [3, 4]])
