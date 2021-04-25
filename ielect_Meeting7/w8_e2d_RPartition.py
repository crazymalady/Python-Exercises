def putRPartition( word ):
    rPart = word.rpartition(word[5]) # rpartition(string)
    print('Word is rpartitioned:', rPart)

def display():
    word = input('Word:')
    putRPartition(word)

display()