#!/bin/python3

def GemstoneFinder():
    """Finds the occurences of gemstones
       using set.intersection() operation
    """
    RockNum = int(input()) # gets the number of rocks
    RockMins = set(input()) # turning first rock into varible
    
    for _ in range(RockNum-1):  # compares 1st rock against other rocks after turning them into variables
        Rocks = set(input())
        RockMins = RockMins.intersection(Rocks) # makes new set with elements that occur in at least one rock
    print(len(RockMins)) # we print the length of our new set to give us the number of gemstones there are
    
GemstoneFinder()
