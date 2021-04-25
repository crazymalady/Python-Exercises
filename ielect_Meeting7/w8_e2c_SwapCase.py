def putSwapCase( word ):
    swCase = word.swapcase()
    print('Word is SwapCase:', swCase)

def display():
    word = input('Word:')
    putSwapCase(word)

display()