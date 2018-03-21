#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:28:32 2018

@author: bijayamanandhar
"""

"""
Description:
What is an anagram? Well, two words are anagrams of each other
if they both contain the same letters. For example:
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""
def anagrams(word, words):
    #your code here
    array = []
    
    word_sorted = sorted(word)
    
    for i in range(len(words)):
        each_word = sorted(words[i])
        
        if each_word == word_sorted:
            array.append(words[i])
            
    return array
    
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
print(anagrams('laser', ['lazing', 'lazy',  'lacer']), [])     

a = ['2','3','1']
a.sort()
print(a)

b = ['2', '4', '5']
c = sorted(b)
print(c)