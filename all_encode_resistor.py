#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:27:07 2018

@author: bijayamanandhar
"""

"""
"10 ohms"        "brown black black gold"
"100 ohms"       "brown black brown gold"
"220 ohms"       "red red brown gold"
"330 ohms"       "orange orange brown gold"
"470 ohms"       "yellow violet brown gold"
"680 ohms"       "blue gray brown gold"
"1k ohms"        "brown black red gold"
"10k ohms"       "brown black orange gold"
"22k ohms"       "red red orange gold"
"47k ohms"       "yellow violet orange gold"
"100k ohms"      "brown black yellow gold"
"330k ohms"      "orange orange yellow gold"
"2M ohms"        "red black green gold"
"""
dict = { 0: 'black', 1: 'brown', 2: 'red', 3: 'orange', 4: 'yellow',\
         5: 'green', 6: 'blue', 7: 'violet', 8: 'gray', 9: 'white', 10:'gold'}

def encode_resistor_colors(n):
    # your code here
    bands = ""

    n = n.split(" ")[0]
    
    if n[-1].isdigit():
        value = float(n)
        
        if value < 10:
            bands = dict[0] +' '+ dict[int(n)] +' '+ dict[0] +' '+ dict[10] 

        elif value < 100:
            bands = dict[int(n[0])] +' '+ dict[int(n[1])] +' '+ dict[0] +' '+ dict[10] 
            
        else:
            bands = dict[int(n[0])] +' '+ dict[int(n[1])] +' '+ dict[1] +' '+ dict[10] 
    
    elif 'k' in n:
        
        if len(n) == 2:
            bands = dict[int(n[0])] +' '+ dict[0] +' '+ dict[2] +' '+ dict[10]
            
        elif len(n) == 3:
            bands = dict[int(n[0])] +' '+ dict[int(n[1])] +' '+ dict[3] +' '+ dict[10]
            
        elif len(n) == 4:
            if n[1] == '.':
                bands = dict[int(n[0])] +' '+ dict[int(n[-2])] +' '+ dict[2] +' '+ dict[10]
            else:
                bands = dict[int(n[0])] +' '+ dict[int(n[1])] +' '+ dict[4] +' '+ dict[10]
    else:
        
        if len(n) == 2:
            bands = dict[int(n[0])] +' '+ dict[0] +' '+ dict[5] +' '+ dict[10]
                        
        elif len(n) == 3:
            bands = dict[int(n[0])] +' '+ dict[int(n[1])] +' '+ dict[6] +' '+ dict[10]
            
        elif len(n) == 4:
            
            if n[-2] == '0': 
                bands = dict[int(n[0])] +' '+ dict[int(n[1])] +' '+ dict[7] +' '+ dict[10]
            else:
                bands = dict[int(n[0])] +' '+ dict[int(n[2])] +' '+ dict[5] +' '+ dict[10]
            
    return bands
     
print(encode_resistor_colors("9 ohms") == "black white black gold", 1)
print(encode_resistor_colors("11 ohms") == "brown brown black gold", 2)
print(encode_resistor_colors("870 ohms") == "gray violet brown gold", 3)
print(encode_resistor_colors("5k ohms") == "green black red gold", 4)
print(encode_resistor_colors("47k ohms") == "yellow violet orange gold", 5)
print(encode_resistor_colors("6.4k ohms") == "blue yellow red gold", 6)
print(encode_resistor_colors("10k ohms") == "brown black orange gold", 7)
print(encode_resistor_colors("330k ohms") == "orange orange yellow gold", 8)
print(encode_resistor_colors("2M ohms") == "red black green gold", 9)
print(encode_resistor_colors("230M ohms") == "red orange violet gold", 11)
print(encode_resistor_colors("2.6M ohms") == "red blue green gold", 12)

def encode_resistor_colors(ohms_string):
    codes = {
            "0": "black", "1": "brown", "2": "red", 
            "3": "orange", "4": "yellow", "5": "green", 
            "6": "blue", "7": "violet", "8": "gray", 
            "9": "white", "5%" : "gold", "10%" : "silver"
            }
            
    ohms_string = (ohms_string.split(" ")[0])
    output = ""
    if "M" in ohms_string:
        ohms_val = int(1000000 * float(ohms_string[:ohms_string.index("M")]))
    elif "k" in ohms_string:
        ohms_val = int(1000 * float(ohms_string[:ohms_string.index("k")]))
    else:
        ohms_val = int(ohms_string)
    vals = str(ohms_val)[0] + str(ohms_val)[1] +  str(len(str(ohms_val))-2)
    for char in vals:
        output += codes[char] + ' '
    return (output + "gold")

    
def encode_resistor_colors(ohms_string):
    cc = ['black','brown','red','orange','yellow','green','blue','violet','gray','white']
    ts = {'k':3, 'M':6}
    r = ohms_string[:-5]

    d = ts.get(r[-1], 0)
    if d > 0: r = r[:-1]
    
    if '.' in r:
        r = r[0] + r[2]
        d -= 1
    elif len(r) > 2:
        r = r[:-1]
        d += 1
    elif len(r) == 1:
        r = r + '0'
        d -= 1

    return '{0} {1} {2} gold'.format(cc[int(r[0])], cc[int(r[1])], cc[d])
    
    
codes = {str(i):c for i, c in enumerate('black brown red orange yellow green blue violet gray white'.split())}
units = {'k':1e3, 'M':1e6}
import re

def encode_resistor_colors(ohms_string):
    pattern = r'^(\d\.?\d*)([kM])? ohms$'
    m = re.match(pattern, ohms_string)
    f = units[m.group(2)] if m.group(2) else 1
    v = str(int(float(m.group(1)) * f))
    return '%s %s %s gold' % (codes[v[0]], codes[v[1]], codes[str(len(v) - 2)])
    
    
def encode_resistor_colors(s):
  ohms = s[:s.index(' ')]
  if   'k' in ohms: a, b, *p = str(int(round(float(ohms[:-1]) * 1e3, 3)))
  elif 'M' in ohms: a, b, *p = str(int(round(float(ohms[:-1]) * 1e6, 6))) # 4.1M
  else:             a, b, *p = ohms
  C = ['black','brown','red','orange','yellow','green','blue','violet','gray','white']
  return ' '.join((C[int(a)], C[int(b)], C[len(p)], 'gold'))
  
  
def encode_resistor_colors(ohms_string):
    color_codes = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "gray", "white"]
    res = ohms_string.split(" ")[0].replace("k","000").replace("M","000000")
    if res.find(".")>0:  res = (res[0:-1]).replace(".","")
    return " ".join( list(map(lambda d: color_codes[d] , [int(res[0]), int(res[1]), len(res)-2]))+["gold"] )
    

    
from math import log10

def encode_resistor_colors(ohms_string):
    codes = {"0": "black", "1": "brown", "2": "red", "3": "orange", "4": "yellow", "5": "green", "6": "blue", "7": "violet", "8": "gray", "9": "white", "k": 1000, "M": 1000000}
    ohms, rest = ohms_string.split()

    if ohms[-1].isalpha():
        magnitude = codes[ohms[-1]]
        ohms = ohms[:-1]
    else:
        magnitude = 1

    first_band = codes[ohms[0]]
    second_band = codes["0" if len(ohms) == 1 else ohms[1] if ohms[1] != "." else ohms[-1]]
    third_band = codes[str(int(log10(float(ohms) * magnitude)) - 1)]

    return "{} {} {} gold".format(first_band, second_band, third_band)
    