#!/bin/python3

n = int(input())

def convertBinary(n):

    # bin() returns a 0b identifier, use [2:] to skip over
    binary_n = bin(n)[2:]
    binary_split = binary_n.split('0')
    
    # since we split by 0, max will return the largest occures of consecutive 1's
    # use count to count the occurences in the string of 1's
    count_1s = max(binary_split).count('1')
    
    print(count_1s)
    
convertBinary(n)
