#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:31:00 2018

@author: bijayamanandhar
"""

""" 01/ reverse string """
def rev_string(text):
    x = []
    y = list(text)
    z = len(text)
    
    while z > 0:
        z -= 1
        x.append(y[z])
    
    return "".join(x)    
print(rev_string("bijaya"))


def string_rev(xyz):
    start = 0
    end = len(xyz)-1
    xYZ = list(xyz)
    
    while start < end:
        temp = xYZ[start]
        xYZ[start] = xYZ[end]
        xYZ[end] = temp
        start += 1
        end -= 1
        
    return "".join(xYZ)    
print(string_rev("12345"))

def rev(x):
    
    temp = []
    i = 0    
    while i < len(x):
        temp += x[-i-1]
        i += 1
        
    return "".join(temp)
print(rev("9876x"))