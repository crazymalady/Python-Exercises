
def display():
    word = "My course is BSIT. BSIT is a great course, isn't it?"
    count = 0
    """
    # using for loop
    for letter in word:
        if letter == 'a':
            count = count + 1
    print('Number of As Detected [FOR]: ', count)"""

    # using while loop
    index = 0
    while index < len(word):
        letter = word[index]
        if letter == 'a' or letter == 'A':
            count = count + 1
        index = index + 1
    print('Number of As Detected [WHILE]: ', count)


    # iterate through sequence of ordered set
    """for letter in 'banana':
        print(letter)"""

display()