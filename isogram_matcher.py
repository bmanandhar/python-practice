#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:13:25 2018

@author: bijayamanandhar
"""


# Isogram Matcher
# ------------------------------------------------------------------------------
# An isogram is a word with only unique, non-repeating letters. Given two isograms
# of the same length, return an array with two numbers indicating matches:
# the first number is the number of letters matched in both words at the same position,
# and the second is the number of letters matched in both words but not in the
# same position.

def isogram_matcher(word1, word2):
    #x-> number of matching letters at the same positions
    #y-> numbers of matching letters at different positions
    x, y = 0, 0

    for i in range(len(word1)):
        if word1[i] == word2[i]:
            x += 1

        for j in range(len(word1)):
            if word1[i] == word2[j]\
            and i != j:
                y += 1

    return [x, y]
print(isogram_matcher("ultrasonic", "ostracized"))
print (isogram_matcher("an", "at") == [1, 0])
print (isogram_matcher("cat", "car") == [2, 0])
print (isogram_matcher("cat", "tap") == [1,1])
print (isogram_matcher("home", "dome") == [3, 0])
print (isogram_matcher("gains", "snake") == [0, 3])
print (isogram_matcher("ultrasonic", "ostracized") == [3, 4])
