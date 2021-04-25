def display():
    try:
        # We can change the values of elements in a List. Lets take an example to understand this.
        # list of nos.
        list = [1,2,3,4,5,6]

        # Deleting 2nd element
        #del list[1]

        # Deleting elements from 3rd to 4th
        #del list[2:4]
        #print(list)

        # Deleting the whole list
        del list
        print(list)

        #if(list == -1):
         #   print("EMPTY!")



    except:
        print("Something went wrong")

display()
