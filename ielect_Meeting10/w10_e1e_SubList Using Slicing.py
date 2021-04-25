def display():
    try:
        # slicing
        list = [1,2,3,4,5,6,7]

        print(list[1:3])

        # list items from beginning to 3rd
        print(list[:3])

        # list items from 4th to end of list
        print(list[3:])

        # Whole list
        print(list[:])

    except:
        print("Something went wrong")

display()
