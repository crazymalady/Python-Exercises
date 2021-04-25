#Removal all the characters other than integersfrom string
"""
Given:

I
am
Julia
17
years and 11
months
old
Expected
Output:
1711

"""

def display():
    str1 = 'I am  Jennifer 17 years and 11 months old'
    index = 0
    for var in str1:
        store = str1[index]
        if ord(store) > 48 and ord(store) < 57:
            print(store, end = "")
        index = index + 1
display()
