#!/bin/python3

# setting 't' which is the number of test cases
# so I can use it for the range
t = int(input())

for x in range(t):
    # since their are multiple 's' being inputed, put it in loop
    s = input()
    # first 's' starts at 0 and prints every 2 spaces (even)
    # second 's' starts at 1 and does same thing (odd) 
    print(s[::2], s[1::2])
