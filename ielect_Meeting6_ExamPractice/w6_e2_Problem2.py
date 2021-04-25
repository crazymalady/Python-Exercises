# Problem 2. A function object is a value you can assign to a variable or pass as an argument.
# For example, do_twice is a function that takes a function object as an argument and calls it twice:
# def do_twice(f):
# 	f()
# 	f()
# Lacaste, Jennifer, 20201029.1131-1147

# 1. Type this example into a script and test it.
"""
2.
def do_twice(fObj, val):
	fObj(val*2)

def print_spam(val):
	print(val)

do_twice(print_spam, 'spam\n')
"""

# 3.Write a more general version of print_spam, called print_twice,
# that takes a string as a parameter and prints it twice.
"""def print_twice(val):
	print(val*2)

print_twice('spam\n')
"""

# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
"""def do_twice(fObj, obj):
	fObj(obj*2)

def print_twice(val):
	print(val)

do_twice(print_twice, 'spam') """

# 5. Define a new function called do_four that takes a function object and a value and calls the
# function four times, passing the value as a parameter.
# There should be only two statements in the body of this function, not four.
def do_four(fObj, val):
	fObj(val*4)

def print_do(val):
	print(val)

do_four(print_do, 'sample\n')



