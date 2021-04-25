"""
by: Lacaste, Jennifer - 2020.10.23"""

def display():
    smallest = 100
    print('Before', smallest)
    list = [9, 41, 12, 3, 15, 74]
    for the_num in list:
        if smallest is None:
            print('Smallest is None:', smallest)
        elif smallest is not None:
            print('Not None:', smallest)
    print(smallest)

display()