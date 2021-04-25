# author    : Lacaste, Jennifer
# createdOn : 20201003
# week      : w2_lab2a
# topic     : VolumeOfSphere
# update    : using functions in Python 'def'
"""The volume of a sphere with radius r is 4/3 πr 3 . What is the volume of a sphere with radius 5?
	Hint: 392.7 is wrong!"""

# formula: V=4/3 (3.14159)radius^3
# input  : V=4/3 (3.14159)5^3

def calcVolumeSphere( radius, unit ):
    power = int(radius) ** 3 #5^3
    # cancellation = round(power/3, 1) #125/3, round of on 1 place
    mul4 = cancellation * 4 #4π41.7
    volume = round(mul4 * 3.14159, 3) #166.8π unit^3

    print('=======================')
    print('Displayed Results')
    print('=======================')
    print('V= 4/3πr^3\n')
    print('V= 4/3π(', radius, ')^3')
    print('V= 4π', cancellation, '^3')
    print('V= ', mul4, 'π', unit, '^3')
    print('____________________________________')
    print('Sphere Volume= ', volume, unit, '^3')
    print('____________________________________')
    print('\nCreated by: Lacaste, Jennifer [from scratch]')

def display():
    print('\nThis is a [Volume Sphere Calculator], Kindly enter the details asked below')
    radius = input('radius: ')
    unit = input('unit: ')
    calcVolumeSphere( int(radius), str(unit) )

display()





"""BASIC START
print('\nThis is a [Volume Sphere Calculator], Kindly enter the details asked below')
radius = input('radius: ')
unit = input('unit: ')
power = int(radius)**3
cancellation = round(power/3, 1)
mul4 = cancellation*4
volume = round(mul4*3.14159, 3)
"""
"""For Debugging and Trial of Function
print('radius is: ', radius )
print('power is: ', power )
print('cancellation is: ', cancellation )
print('mul4 is: ', mul4 )
print('Sphere Volume is: ', volume )
"""
"""
print('=======================')
print('Displayed Results')
print('=======================')
print('V= 4/3πr^3\n')
print('V= 4/3π(', radius, ')^3')
print('V= 4π', cancellation, '^3')
print('V= ',mul4, 'π', unit, '^3')
print('____________________________________')
print('Sphere Volume= ', volume, unit, '^3' )
print('____________________________________')
print('\nCreated by: Lacaste, Jennifer [from scratch]')
"""