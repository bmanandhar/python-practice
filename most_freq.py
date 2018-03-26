#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 15:49:49 2018

@author: bijayamanandhar
"""

'''
This program will find out the most frequest element
in a python list by creating a dictionary
'''

def most_freq(list):

    count = {}
    max_count = 0
    max_item = None

    for i in list:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
            if count[i] > max_count:
                max_count = count[i]
                max_item = i
                
    return 'Most frequent: {} \nFrequency: {}'.format(max_item, max_count)

print(most_freq([1,1,2,3,3,3,1,1]))
