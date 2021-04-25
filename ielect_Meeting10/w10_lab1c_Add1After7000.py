def display():
    try:
        # 3. Create a python program that will add item 1 after 7000 in the following Python List
        list1 = [100, 220,[300, 400,[5000, 7000],500],30, 40]

        list1[2][2].append("1")
        print(list1)

    except:
        print("Something went wrong")

display()
