"""
by: Lacaste, Jennifer - 2020.10.23"""

def display():
    cnt = 0
    sum = 0
    print('Before', cnt, sum)
    for value in [9, 41, 12, 3, 74, 15]:
        sum = sum + value
        print(cnt, sum, value)
        cnt = cnt + 1
    print('After', cnt, sum, sum / cnt)

display()
