# From given string replace each punctuation with #
# Given:
# str1 = '/*Jon is @developer & musician!!'
"""
/-47
*42
&38"""

def display():
    str1 = '/*Jon is @developer & musician!!'

    # ascii table of chars is less than 48
    index = 0
    x = None
    str6 = None
    for asc in str1:
        cont = str1[index]
        if cont == '/':
            x = str1.replace(str1[index], '#')
            str2 = x
        if cont == '*':
            x = str2.replace(str1[index], '#')
            str3 = x
        if cont == '@':
            x = str3.replace(str1[index], '#')
            str4 = x
        if cont == '&':
            x = str4.replace(str1[index], '#')
            str5 = x
        if cont == '!':
            x = str5.replace(str1[index], '#')
            str6 = x
        index = index + 1
        """if ord(cont) < 47:
            x = str1.replace(cont, '#')"""
            # 35 is ascii of #
    print(str6)
display()