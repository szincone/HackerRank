#!/bin/python3

import os
import sys

def diagonalDifference(a):
    """ adds then finds the absolute
        difference between two different
        diagonals.
    """
    f_diag = 0 # creatings empty score vars
    s_diag = 0
    
    for x in range(n): # since diagonals are (0,0), (1,1), and so-on; use a forloop to add our diagonals
        f_diag += a[x][x] # hackerrank input uses 'a' for matrix's rows
        s_diag += a[x][len(a[0])-1-x] # same things as above, just going backward for column
        
    return abs(f_diag-s_diag) # returns absoulute difference between our diagonals
