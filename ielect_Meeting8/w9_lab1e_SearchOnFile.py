#Lab5 5 Write a python  program that will search all Terrier in the file.

def searchInFile(file, name):
    fhand = open(file) #filename from input

    count = 0

    for line in fhand:
        if line.startswith(name):
            count = count + 1
            print(line)
        count = count + 1

    print('There are', count, name,'lines in', fhand.name)

def display():
    try:
        file = input('File Name: ')

        if file.__contains__('.') and (file == "dog_breeds.txt" or 'mbox-short.txt') :
            name = input('Search: ')
            searchInFile(file, name)
        else:
            print('Sorry invalid filetype or File Not Found')
    except:
        print('Something went wrong!')

display()








































