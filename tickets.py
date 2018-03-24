#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:15:28 2018

@author: bijayamanandhar
"""

def tickets(people):
    """Check if clerk can sell all tickets and give the charge
    Args:
        people (list): List of bills, where bill belongs to [25, 50, 100]
    Returns:
        str: 'YES' or 'NO'
    Examples:
        >>> tickets([25, 25, 100])
        'NO'
        >>> tickets([25, 25, 50, 100])
        'YES'
    """
    bill_25, bill_50 = 0, 0

    for bill in people:
        if bill == 25:
            bill_25 += 1
        elif bill == 50 and bill_25:
            bill_25 -= 1
            bill_50 += 1
        elif bill == 100 and bill_50 and bill_25:
            bill_25 -= 1
            bill_50 -= 1
        elif bill == 100 and bill_25 > 2:
            bill_25 -= 3
        else:
            return 'NO'
    return 'YES'