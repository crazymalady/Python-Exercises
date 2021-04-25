# author    : Lacaste, Jennifer
# createdOn : 20201008
# week      : w3_labC
# topic     : PassORFailed

"""3. Write a python program that prompts students enter for their
prelim, midterm and finals grade in the subject “Intro. Machine Language”).
Print the average whether  they have pass or failed. (At PCC grade lower than 74 are failed.)
"""

# should return only 1 result
def calcGrade( name, prelim, midterm, finals ):
    total = float(prelim+midterm+finals)
    average = float(round(total/3, 1))

    # grade greater than 90
    if average >= 90 or average >= 80 or average >= 74 or average == 100:
        print('\n', name, "'s Grade Results\n--------------------------------------------------------")
        print('Average is: ', average, '\nStatus:', name, "Passed!\n--------------------------------------------------------")
    # grade less than 90
    elif average < 74:
        print('\n',name, "'s Grade Results\n--------------------------------------------------------")
        print('Average is: ', average, '\nStatus:', name, "Failed!\n--------------------------------------------------------")
    else:
        print(name, "'s Grade Results\n--------------------------------------------------------")
        print('\n','Average is: ', average, '\nStatus:', name, "Failed!\n--------------------------------------------------------")

    return average

def display():
    print('This program is to check if a PCC Student passed or failed================\nin Intro to Machine Language')
    print('Enter the grade details===================================================')

    name = input('Student Name: ')
    prelim = float( input('Prelim: ') )
    midterm = float(input('Mid-term: '))
    finals = float(input('Finals: '))

    calcGrade( name, prelim, midterm, finals )

display()