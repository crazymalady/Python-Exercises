# author    : Lacaste, Jennifer
# createdOn : 20201008.1226-1227
# week      : w3_labA
# topic     : Even Or Odd

"""1. Write a python program to check whether a number is even or odd using if else. Inputs are from the user"""

def evenOrOdd( num ):
    if num%2 == 0 :
        print('Result: even')
    else:
        print('Result: odd')

def display():
    num = float(input('Number: '))
    evenOrOdd( num )

display()

