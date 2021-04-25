"""
Create a program to display student's marks from record
"""

def displayGrades(studName):
    #key = 1
    marks = {"Jeuz":90,"Jules":55,"Arthur":77}
    for student in marks:
        if studName == student:
            print(student, marks.get(studName))
            #key == -1
            break
    else:
        print('No data found.')

def display():
    studName = input('Student Name: ')
    displayGrades(studName)

display()



