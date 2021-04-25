
def display():
    try:
        fruit = input('Fruit:')
        choice = int(input('Num Choice:'))
        fArray = fruit[0]   # array
        mArray = fruit[choice]      # get the letter based on the user input

        print('fArray: ', fArray.upper())

        # modified using an input
        if choice > len(fruit):
            print("Sorry length exceeded!")
        elif choice <= len(fruit):
            print('mArray: ', mArray.upper())
    except:
        if choice > len(fruit):
            print("Sorry length exceeded!")

display()