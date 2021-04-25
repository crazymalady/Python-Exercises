#Lab1 Write a python program to read dog_breed.txt.


#with loop
"""count = 0

for getTXT in fhand:
    rr = fhand.read()
    print(rr)
    count = count + 1
"""
def display():
    rr = ''
    print('File Read from another function： \n' + readFile(rr))

def readFile(rr):
    fhand = open('dog_breeds.txt')
    rr = fhand.read()
    return rr

display()














































