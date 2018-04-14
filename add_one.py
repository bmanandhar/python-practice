# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
Write a python program returns as follows:
[1,2,3] --> [1,2,4],
[2,5,9] --> [2,6,0],
[3,9,9] --> [4,0,0],
[9,1,9,9] --> [9,2,0,0] and
[9,9,9,9] --> [1,0,0,0,0] 
'''

def add_one(array):
    carry = 1
    #iterates from the end of array
    for i in range(len(array) -1, -1, -1):
        total = array[i] + carry
        if total % 10 == 0:
            array[i] = 0
        else:
            carry = 0 
            array[i] = total % 10
    #checks if carry is still 1 after final iteration
    if carry == 1:
        array = [1] + array                  
    return array

print(add_one([1,2,3]) == [1,2,4])
print(add_one([2,5,9]) == [2,6,0])
print(add_one([3,9,9]) == [4,0,0])
print(add_one([9,1,9,9]) == [9,2,0,0])
print(add_one([9,9,9,9]) == [1,0,0,0,0])
