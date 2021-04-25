# author    : Lacaste, Jennifer
# createdOn : 20201008.1221
# week      : w3_exercise1h
# topic     : Grade

def calcGrade( score ):
    if score >= 90:
        print( 'grade: A' )
    elif score >= 80: #B
        print('grade: B')
    elif score >= 70:  # c
        print( 'grade: C' )
    elif score >= 60:  # D
        print( 'grade: D' )
    else:  # F
        print( 'grade: F' )

def display():
    score = float( input('Score: ') )
    print('Enter Score: ', score)
    calcGrade( score )
display()