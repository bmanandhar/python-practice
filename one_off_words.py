#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:30:09 2018

@author: bijayamanandhar
"""

def one_off_words(word, words):

    finals = []
    for i in range(len(words)):
        one_word = words[i]

        if one_off(word, one_word):
            finals.append(one_off(word, one_word))

    return finals
    
def one_off(word, one_word):

    count = 0

    if word != one_word:
        if len(word) == len(one_word):
            for i in range(len(word)):
                if word[i] != one_word[i]:
                    count += 1

            if count < 2:                 
                return one_word 
  
print(one_off_words('moor', ["moot", "door", "boot", "boots"]) \
                == ['moot', 'door'])