#!/bin/python3

# get variable inputs and make empty string to push new 'array' too.
n = int(input())
# got to split it for the bigger numbers in the hidden test cases
arr = input().split()
reversed_arr = ""

# iterate over every element in array, one by one, we start at 0 and subtract
# by one each time, this will reverse the array because -1 is end of array
for n in arr[::-1]:
    # push results to new empty string
    reversed_arr += str(n) + " "
    
print(reversed_arr)


    
