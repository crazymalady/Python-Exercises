#Lab3 Write a python program that will append the file (dogs_breeds.txt)Put your name on it.

def display():
    readFile()

def readFile():
    # Append-adds at last
    dfile = open("dog_breeds.txt", "a")
    dfile.write("Jennifer Lacaste \n")
    dfile.close()

    dfile = open("dog_breeds.txt", "r")
    #output the updated
    print(dfile.read())
    dfile.close()


display()














































