#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:44:12 2018

@author: bijayamanandhar
"""

# 06 Morse Encode

# Build a function, `morse_encode(str)` that takes in a string (no
# numbers or punctuation) and outputs the morse code for it. See
# http://en.wikipedia.org/wiki/Morse_code. Put two spaces between
# words and one space between letters.
#
# You'll have to type in morse code: I'd use a hash to map letters to
# codes. Don't worry about numbers.
#
# I wrote a helper method `morse_encode_word(word)` that handled a
# single word.
#
# Difficulty: 2/5

CODE = {'A': '.-',	 'B': '-...',   'C': '-.-.',
		'D': '-..',	'E': '.',	  'F': '..-.',
		'G': '--.',	'H': '....',   'I': '..',
		'J': '.---',   'K': '-.-',	'L': '.-..',
		'M': '--',	 'N': '-.',	 'O': '---',
		'P': '.--.',   'Q': '--.-',   'R': '.-.',
		'S': '...',	'T': '-',	  'U': '..-',
		'V': '...-',   'W': '.--',	'X': '-..-',
		'Y': '-.--',   'Z': '--..'}

# 

def morse_encode(str):
	 word_arr = str.split()
	 morse_arr = [ morse_encode_word(word) for word in word_arr ]
	 return "  ".join(morse_arr).strip()

def morse_encode_word(word):
	letters = list(word) # Pythonic way to split word into letters
	code = [ CODE[letter.upper()] for letter in letters ]
	return " ".join(code)

print("Test for morse encode")
print(morse_encode("cat") == "-.-. .- -")
print(morse_encode("cat in hat")  == "-.-. .- -  .. -.  .... .- -")
print("==  ==  ==  ==  ==  ==")