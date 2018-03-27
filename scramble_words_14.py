#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 09:13:45 2018

@author: bijayamanandhar
"""

def scramble_string(string, positions):
    result = ''
    for i in range(len(positions)):
        result += string[positions[i]]
    return result
print(scramble_string('ebdcaf', [4, 1, 3, 2, 0, 5]))

""" for while loop """

def scramble_string(string, positions):

    result = ''

    i = 0
    while i < len(string):
        result += string[positions[i]]
        i += 1

    return result
print(scramble_string('ebdcaf', [4, 1, 3, 2, 0, 5]))

# function-2:

import random
def scramble_string(string):
    x = ''
    y = len(string)
    ind = random.sample(range(y), y)

    for i in range(y):
        x += string[ind[i]]
    return x

print(scramble_string('abcd'))

'''
def scramble_string(string, positions)
  result = ""

  i = 0
  while i < positions.length
    result = result + string[positions[i]]
    i += 1
  end

  return result
end

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

puts(
  'scramble_string("abcd", [3, 1, 2, 0]) == "dbca": ' +
  (scramble_string("abcd", [3, 1, 2, 0]) == "dbca").to_s
)
puts(
  'scramble_string("markov", [5, 3, 1, 4, 2, 0]) == "vkaorm"): ' +
  (scramble_string("markov", [5, 3, 1, 4, 2, 0]) == "vkaorm").to_s
)
'''
