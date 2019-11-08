# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
Write a python program that returns as follows:

[0] --> [1],
[7,2,0] --> [7,2,1],
[2,5,9] --> [2,6,0],
[3,9,9] --> [4,0,0],
[9,1,9,9] --> [9,2,0,0] and
[9,9,9,9] --> [1,0,0,0,0]
'''

def add_one(array):
    carry = 1
    #iterates from the end of array back
    for i in range(len(array) -1, -1, -1):
        total = array[i] + carry
        if total % 10 == 0:
            array[i] = 0
        else:
            carry = 0
            array[i] = total % 10
    #checks if carry is still 1 after final iteration
    if carry == 1:
        array = [carry] + array
    return array

print(add_one([0]) == [1], " #No-1")
print(add_one([7,2,0]) == [7,2,1], " #No-2")
print(add_one([2,5,9]) == [2,6,0], " #No-3")
print(add_one([3,9,9]) == [4,0,0], " #No-4")
print(add_one([9,1,9,9]) == [9,2,0,0], " #No-5")
print(add_one([9,9,9,9]) == [1,0,0,0,0], " #No-6")
