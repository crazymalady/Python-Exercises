#Lab2 Write a python program that will read the first three lines of the file (dog_breeds.txt)

def display():
    readFile()

def readFile():
    fhand = open('dog_breeds.txt')
    count = 0
    numLines = 3
    while count < numLines:
        dline = fhand.readline()
        print(dline)
        count = count + 1
    return dline


display()














































