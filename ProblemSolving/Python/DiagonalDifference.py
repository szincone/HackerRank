#!/bin/python3

import os
import sys

def diagonalDifference(a):
    f_diag = 0
    s_diag = 0
    
    for x in range(n):
        f_diag += a[x][x]
        s_diag += a[x][len(a[0])-1-x]
        
    return abs(f_diag-s_diag)
