#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:33:31 2018

@author: bijayamanandhar
"""

# 05 Wonky Coins

# Catsylvanian money is a strange thing: they have a coin for every
# denomination (including zero!). A wonky change machine in
# Catsylvania takes any coin of value N and returns 3 new coins,
# valued at N/2, N/3 and N/4 (rounding down).
#
# Write a method `wonky_coins(n)` that returns the number of coins you
# are left with if you take all non-zero coins and keep feeding them
# back into the machine until you are left with only zero-value coins.

def wonky_coins(n):
    n = int(n)
    
    if n == 0: return 1
    else:
        return wonky_coins(n/4) + wonky_coins(n/3) + wonky_coins(n/2)
    
    
print("= = = = Wonky Coins = = = =")    
print('<n =1>', wonky_coins(1))
print('<n =3>', wonky_coins(3))
print('<n =4>', wonky_coins(4))
print('<n =5>', wonky_coins(5))
print('<n =6>', wonky_coins(6))
print('<n =7>', wonky_coins(7))

print("= = = = = = = = = =")
