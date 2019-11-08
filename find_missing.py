#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:22:10 2018

@author: bijayamanandhar
"""
# Find the missing number in the array

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 10:00:38 2019

@author: bijayamanandhar
"""

# =============================================================================
# def anagram(word1, word2):
#     
#     if helper(word1) == helper(word2):
#         return "'{}' and '{}' are anagrmas to each other.".format(word1, word2)
#     else:
#         return False
#     
#     
#     
# def helper(word):
#     
#     arr = [None]*len(word)
#     for i in range(len(word)):
#         arr[i] = word[i]
#     return sorted(arr)
# 
# print(anagram("word", "row"))
# =============================================================================
        
# =============================================================================
# def CheckNums(num1, num2):
#     x = None
#     if num2 > num1:
#         x = 'true'
#         
#     elif num2 < num1:
#         x = 'false'
#         
#     else: x = -1
#     
#     return x
# 
# # keep this function call here  
# print (CheckNums(4, 7) == 'true')   
# print (CheckNums(9, 1) == 'false') 
# print (CheckNums(5, 5) == -1) 
# =============================================================================
def missing(arr):
    
    for i in range(len(arr) -1):
        if i > 0:
            left = arr[i] -arr[i -1]
            right = arr[i +1] -arr[i]
            if left != right:
                return int(arr[i] +arr[i +1])/2
                
print(missing([1, 2, 3, 4, 6, 7, 8, 9]) == 5)
print(missing([9, 7, 5, 3, -1, -3]) == 1)
print(missing([10, 15, 25, 50, 35]) == 20)
print(missing([0, -3, -6, -12, -15, -18]) == -9)
