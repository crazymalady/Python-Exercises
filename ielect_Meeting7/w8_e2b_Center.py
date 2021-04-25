def putCenter( word ):
    mid = word.center(10) # center(padding)
    print('Word is Center:', mid)

def display():
    word = input('Word:')
    putCenter(word)

display()