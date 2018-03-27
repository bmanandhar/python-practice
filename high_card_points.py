#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:52:06 2018

@author: bijayamanandhar
"""

def high_card_points(hand):

    points = 0
    for i in hand:

        if i == "J":
            points += 1

        elif i == "Q":
            points += 2

        elif i == "K":
            points += 3

        elif i == "A":
            points += 4

    return points
print(high_card_points(["2","3","4","5","6","7","8","9","10","J","Q","K","A"]))
