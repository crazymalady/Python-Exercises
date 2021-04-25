# Write a function called guessTheNumber that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify the even
# and odd numbers. For example, if the limit is 5, it should print:
# 0 EVEN
#	1 ODD
#	2 EVEN
#	3 ODD
#	4 EVEN
#	5 ODD
# Note: Limit should be from the user input
# Lacaste, Jennifer, 20201029.1131-1147

def guessTheNumber( limit ):
    num = 0
    while num <= limit:
        if num%2==0:
            print(num, 'EVEN')
        elif num % 2 != 0:
            print(num, 'ODD')
        num += 1

def display():
    try:
        limit = int(input('Input Limit: '))
        guessTheNumber(limit)
    except:
        print('Please Enter a Valid Input! (int)')

display()
