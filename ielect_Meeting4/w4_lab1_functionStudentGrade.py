"""3.Create a function student() in such a way that it should accept student name,
and it’s grades and display both, and if the grade is missing in function call it should
show it as 70."""

def studentInfo( name, grade ):
    print( 'Student info is:\n', name, '\n', grade )
    #print('Student info is:\n', name, '\n', 70)

def display():
    try:
        studName = input('Name: ')
        grade = float(input('Grade: '))
        studentInfo( studName, grade )
    except:
        studentInfo(studName, 70)
        print("Please insert a valid number. Currencies cannot contain commas, spaces, or characters.")

display()
