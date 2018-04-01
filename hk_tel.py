#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 07:02:39 2018

@author: bijayamanandhar
"""
# "1234 5678"
def hk_tel(n): 
    if n[:4].isdigit() and n[5:10].isdigit() and n[4] == " " and len(n) == 9:
        return True
    else:
        return False
print(hk_tel('1234 5678'))
