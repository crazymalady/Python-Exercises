def display():
    try:
        # We can change the values of elements in a List. Lets take an example to understand this.
        # list of nos.
        list = [1,2,3,4]

        # changing val of 3rd item
        list[2] = "Burger"

        # Changing the values of 2nd to fourth items
        list[1:4] = [11,22,"Burger"]
        print(list)


    except:
        print("Something went wrong")

display()
