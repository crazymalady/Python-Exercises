"""
by: Lacaste, Jennifer - 2020.10.23"""

def display():
    zork = 0
    print('Before', zork)
    for thing in [9, 41, 12, 3, 74, 15]:
        zork = zork + thing
        print(zork, thing)
    print('After', zork)

display()