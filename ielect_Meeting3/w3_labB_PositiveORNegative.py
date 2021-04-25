# author    : Lacaste, Jennifer
# createdOn : 20201008.1226-1227
# week      : w3_labB
# topic     : Positive or negative
"""2.Write a python program to check positive, negative or zero using simple if or if else."""
def posOrNega( num ):
    if num == 0:
        print(' That is a ZERO NUMBER')
    if num > 0:
        print(' That is a POSITIVE NUMBER')
    if num < 0:
        print(' That is a NEGATIVE NUMBER')

def display():
    print("Check if num is positive of negative-----" )
    num = float( input('Number: ') )
    posOrNega( num )

display()



