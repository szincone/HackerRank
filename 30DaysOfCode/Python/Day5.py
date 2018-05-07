#!/bin/python3

n = int(input())
# HackerRank variable

def Loops(n):
    """ Prints 10 lines of output, containing n*x. """
    for x in range(1, 11):
        print(str(n) + " x " + str(x) + " = " + str(int(n * x)))

Loops(n)
