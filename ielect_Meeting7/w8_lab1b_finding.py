# Find all occurrences of “BSIT” in given string ignoring the case
def display():
    word = "My course is BSIT. BSIT is a great course, isn't it?"
    count = 0
    sp = word.split()

    ind = {}
    for var in sp:
        ind[var] = ind.get(var, 0) + 1
    print(ind.get('BSIT'))

display()