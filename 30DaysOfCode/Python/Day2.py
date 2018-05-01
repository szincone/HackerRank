#!/bin/python3

def total():
    """ Finds the total cost of the meal
        after tax and tip.
    """
    
    meal_cost = float(input()) # makings variables
    tip_percent = int(input())
    tax_percent = int(input())

    totalCost = meal_cost + (meal_cost * (tip_percent/100)) + (meal_cost * (tax_percent/100)) # getting total cost
    
    print('The total meal cost is ' + str(round(totalCost)) + ' dollars.') # printing total
    
total()
