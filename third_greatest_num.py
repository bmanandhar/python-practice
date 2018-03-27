# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def third_greatest_num(num_list):

    num_list.sort()

    return num_list[-3]

print("-------------------------")
print(third_greatest_num([2, 5, 1, 6, -3]) == 2)
print(third_greatest_num([0, -9, 9, 4,1]) == 1)
print("-------------------------")

#This line being added for test
#======
def third(numList):

    i, ii, iii = None, None, None

    for x in numList:

        if i == None or x > i:
            iii, ii, i = ii, i, x

        elif ii == None or x > ii:
            iii, ii = ii, x

        elif iii == None or x > iii:
            iii = x

    return iii

print('   --------------    ')
print(third([2, 5, 1, 6, -3]) == 2)
print(third([-2, 5, 0, 6, 3]) == 3)
print(third([0, 3, 0, 9, 2, 8]) == 3)
print('   --------------    ')
