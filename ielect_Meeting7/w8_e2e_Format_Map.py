def putFormat_Map( word ):
    format_MapYes = '{f} {yes}' .format_map(word)
    format_MapNo = '{f} {no}'.format_map(word)

    print('Word is formatMapYes:', format_MapYes)
    print('Word is formatMapNo:', format_MapNo)

def display():
    word = {'f': "jennifer", 'yes':'very cute', 'no':'very ugly' } #word = input('Word:')
    putFormat_Map(word)

display()
