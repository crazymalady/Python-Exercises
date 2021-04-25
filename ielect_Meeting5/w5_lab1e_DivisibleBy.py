"""
Given a list iterate it and display numbers which are
divisible by 10 and if you find number greater than 200
stop the loop iteration

list1 = [120, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
created by: Lacaste, Jennifer - 2020.10.23"""


def f_divisibBy10():
    sList = [120, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200, 205]
    length = len(sList)
    for cnt in range(length):
        cont = str(sList[cnt]).__contains__('0')    # If it contains 0 it returns true
        if sList[cnt] > 200:
            break
        if cont == True:
            # get the index of 0 that should be at the end only (e.g what if there's 205?)
            # display num that contains it
            print(sList[cnt])

f_divisibBy10()
