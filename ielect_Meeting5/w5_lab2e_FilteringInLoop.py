"""
by: Lacaste, Jennifer - 2020.10.23"""

def display():
    val = None # no val for now
    print('Before')
    for value in [9, 41, 12, 3, 74, 15]: # 3
        if value > 20:
            print('Large Number', value)
            val = value # store here ahahaha.

    print('After', val)

display()
