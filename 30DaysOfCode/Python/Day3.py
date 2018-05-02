#!/bin/python3

def weird_checker():
    """ Determines if a number is
        'weird' or not.
    """
    n = int(input())
    if n % 2 == 0 and n > 20:
        print('Not Weird')
    elif n > 2 and n < 5 and n % 2 == 0:
        print('Not Weird')
    else:
        print('Weird')

weird_checker()
