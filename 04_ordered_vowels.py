#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:31:52 2018

@author: bijayamanandhar
"""
# 04 Ordered Vowel Words
# "This function returns the words
# that have vowels in order 'aeiou'."
class Solution:

	def ordered_vowel_words(self, str):
		ordered_words = ""
		for word in str.split():
			if self.ordered_vowel_word(word):
				ordered_words += word + " "
		return ordered_words.strip()

	def ordered_vowel_word(self, word):
		vowels = 'aeiou'
		last_vowel = ''
		for char in word:
			if char in vowels:
				if char >= last_vowel:
					last_vowel = char
				else:
					return False
		return True

if __name__ == '__main__':

	S = Soluti	on()

	phrases = [
            "this is a test of the vowel ordering system",
			"tests for ordered vowel words",
			"amends state human", # == "amends state"
			"These are complicated stuff", # == "These are stuff"
			"afoot", # == "afoot"
			"ham got hit", # == "ham got hit"
			"crypt", # == "crypt"
			"o", # == "o"
			"tamely", # == "tamely"
			"ccv"
			]		

	for phrase in phrases:
		print(S.ordered_vowel_words(phrase))



