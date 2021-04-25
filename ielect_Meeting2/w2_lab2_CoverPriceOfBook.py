# author    : Lacaste, Jennifer
# createdOn : 20201003
# week      : w2_lab2b
# topic     : Cover Price of a Book with Discounts
# updated   : using functions in Python 'def'
"""Suppose the cover price of a book is P50, but bookstores get a 50% discount.
   Shipping costs P10 for the first copy and P5 for each additional copy. What is the
   total wholesale cost for 60 copies?"""

def calcWholesale():
    orig_price = 50
    discount = orig_price * (50 / 100)
    disc_price = orig_price - discount
    shippingCost = 10 + (5 * (orig_price - 1))
    wholesale = disc_price * 60 + shippingCost
    return wholesale

def display():

    print('This is [Book Cover Whole Sale Problem]')
    print( 'Wholesale of 60 copies= P', calcWholesale())
    footerOutro()

def footerOutro():
    print('\n---------------------------------------------------')
    print('   Created by: Lacaste, Jennifer [from scratch]')
    print('---------------------------------------------------')
display()


"""
orig_price = 50
discount = orig_price*(50/100)
disc_price = orig_price - discount
shippingCost = 10 + (5 * (orig_price - 1)) #price - 1 = 59
wholesale = disc_price * 60 + shippingCost

print( 'wholesale = ', wholesale )"""





