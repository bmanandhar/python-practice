#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:52:06 2018

@author: bijayamanandhar
"""

def high_card_points(hands):

    points = 0
    for i in range(len(hands)):

        if hands[i] == "J":
            points += 1

        elif hands[i] == "Q":
            points += 2

        elif hands[i] == "K":
            points += 3

        elif hands[i] == "A":
            points += 4

    return points
print(high_card_points(["2","3","4","5","6","7","8","9","10","J","Q","K","A"]))
