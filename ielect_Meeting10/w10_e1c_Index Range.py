def display():
    try:
        num = int(input("Access: "))
        intList = [1,2,3]
        range = len(intList)

        if(num > range):
            print("Error! Exceeded!")
        else:
            print("Float List: ", intList[num]) #access specific index

    except:
        print("Something went wrong")

display()
