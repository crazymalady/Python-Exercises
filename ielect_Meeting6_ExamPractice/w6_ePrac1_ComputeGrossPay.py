# Write a program to prompt the user for hours and rate per hour
# to compute gross pay.
# Lacaste, Jennifer

def calcGross( hrs, rate ):
    gross = hrs * rate
    print('Gross Pay: ', gross)
    return gross

def display():
    try:
        hours = int(input('Hours: '))
        rate = float(input('Rate: '))
        calcGross( hours, rate )
    except:
        print('Please Enter a Valid Input!')

display()

