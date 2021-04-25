"""4. Create a function calculation() such that it can accept two variables and calculate
the addition and subtraction of it. And also it must return both addition and subtraction
in a single return call ."""

def calculation( num1, num2 ):
    #addition
    add = num1 + num2
    print( num1, '+', num2, ' = ', add )
    #subtraction
    sub = num1 - num2
    print(num1, '-', num2, ' = ', sub)

def display():
    try:
        num1 = float(input('Num1: '))
        num2 = float(input('Num2: '))
        calculation( num1, num2 )
    except:
        print( 'Please enter an appropriate value' )

display()