""" Print
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5"""

nos = 5
for rows in range(1, nos+1 ):
    for cols in range(1, rows+1):
        print(cols, end = " ") #need this to stay in line!!!
    print()



