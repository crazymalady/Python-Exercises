"""
Accept number from user and calculate the sum of all number between 1 and given number,
(For example user given 10 so the output should be 55)"""
"""for range parameter
   range(start, stop[, step])
   """

def calcSum(rangeNum):
    sum = 0
    for rows in range(0, rangeNum+1, 1):
        sum = sum + rows
    print(sum)


def display():
    rangeNum = int(input('Number: '))
    calcSum(rangeNum)

display()




