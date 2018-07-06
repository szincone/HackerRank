#!/bin/python3
import math;

n = int(input())
def factorial(n):
    # get the factorial of 1 and 0, since it's 1
    if n <= 1:
        print(1)
    # get the factorial of any number not 1 or 0
    else:
        result = n * math.factorial(n - 1)
        print(result)
    
factorial(n);
