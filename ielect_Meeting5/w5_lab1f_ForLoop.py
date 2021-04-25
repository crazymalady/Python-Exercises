"""
Display a message “jeuz” after successful execution of for loop
For example, the following loop will execute without any error.
for i in range(5):
    print(i)
So the Expected output should be:

0
1
2
3
4
jeuz!
by: Lacaste, Jennifer - 2020.10.23"""


def f_forLoop(r):
    for cnt in range(r):
        print(cnt)
    print('Jeuz!')

def display():
    key = 1 # means continue/break, entering
    while key == 1:
        try:
            range = int(input('Range: '))
            f_forLoop(range)
        except:
            print('Sorry, Please Input a Valid Range!')
            cont = input('Do you still want to continue? Y/N: ')
            try:
                if cont == 'y' or cont == 'Y':
                    key == 1
                    continue
                elif cont == 'n' or cont == 'N':
                    key == -1
                    break
            except:
                print('Sorry, Please Input a Valid Range!')
                key == 1
                continue
display()
