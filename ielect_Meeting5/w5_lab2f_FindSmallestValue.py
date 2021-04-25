"""
by: Lacaste, Jennifer - 2020.10.23"""

def display():
    small = None # arbitrary
    list = [9, 41, 12, 3, 15, 74]
    for the_num in list:
        smallest_so_far = list[0]
        print('Before', smallest_so_far)
        if the_num < smallest_so_far:
            smallest_so_far = the_num
            print('Smallest', smallest_so_far)
            small = smallest_so_far
    print('After', small)

display()