

def banana( word ):
    if word == 'banana':
        print('All right, bananas.')
    elif word < 'banana':
        print('Your word ,' + word + ', comes before banana.')
    elif word > 'banana':
        print('Your word ,' + word + ', comes after banana.')
    else:
        print('All right, bananas.')

def display():
    word = input('Word:')
    banana(word)

display()