#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 10:09:19 2018

@author: bijayamanandhar
"""

def encrypt(str):
    str = str + " "
    str = list(str)
    print(str)

    temp = ""
    char, final = [], []

    for i in range(len(str) -1):
        temp += str[i]

        if i > 0:
            if str[i +1] != str[i]:

                char.append(temp[0])
                char.append(len(temp))
                final.append(char)
                char = []
                temp = ""

    return final
print(encrypt("aaabc"))


'''
Here's an example of the method:

WORDS = ["door", "moot", "boot", "boots"]
one_off_words("moor", WORDS) == ["door", "moot"]
'''


def encrypt(str):
    temp = ""
    i = 0
    while i < len(str):
        while str[i] == str[i +1]:
            temp += str[i]
        i += 1
    return temp
print(encrypt("aabbccc"))


