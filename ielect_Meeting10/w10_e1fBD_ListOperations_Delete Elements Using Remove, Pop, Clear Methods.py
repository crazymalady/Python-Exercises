def display():
    try:
        # list of chars
        ch = ["A", "E", "I", "O"]

        # Deleting the element with value 'E'
        ch.remove('E')
        #print("ch is: ", ch)

        # Deleting 2nd element
        ch.pop(1) # numerical val for arg.

        # Deleting all the elements
        ch.clear()
        print("ch is: ", ch)

    except:
        print("Something went wrong")

display()
