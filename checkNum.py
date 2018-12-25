#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 18:03:40 2018

@author: bijayamanandhar
"""

'''
Challenge
Using the Python language, have the function
CheckNums(num1,num2) take both parameters being
passed and return the string true if num2 is
greater than num1, otherwise return the string false. 
If the parameter values are equal to each other 
then return the string -1. 

'''

def CheckNums(num1,num2): 

    # code goes here 
    x = None
    if num2 > num1:
        x = 'true'
    elif num2 < num1: 
        x = 'false'
    else:
        x = -1
    return x
    
# keep this function call here  
print (CheckNums(4, 7) == 'true')   
print (CheckNums(9, 1) == 'false') 
print (CheckNums(5, 5) == -1) 