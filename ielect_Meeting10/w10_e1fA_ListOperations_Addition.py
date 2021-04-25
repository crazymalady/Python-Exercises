def display():
    try:
        # There are several ways you can add elements to a list.
        # list of nos.
        list = [1,2,3,4]

        # 1. adding item at the desired location
        # adding element 100 at the fourth location
        list.insert(3, 100) # (location, data to be added)
        print(list)

        # 2. adding element at the end of the list
        list.append(99)
        print(list) # data added from previous will still be included with the new appended data

        # 3. adding several elements at the end of list
        # the following statement can also be written like this:
        # n_list + [11, 22]
        list.extend([11,22])
        print(list)


    except:
        print("Something went wrong")

display()
