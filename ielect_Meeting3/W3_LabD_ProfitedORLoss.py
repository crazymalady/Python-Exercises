# author    : Lacaste, Jennifer
# createdOn : 20201008
# week      : w3_labD
# topic     : Profit OR Loss

"""
4. Write a Python program to input cost price and selling price of a product and check profit or loss.
Also calculate total profit or loss using if else.
E.G Input; Input cost price: 1000, Input selling price: 1500; Output; Profit: 500"""

def display():
    costPrice = float(input('Cost Price: '))
    sellingPrice = float(input('Selling Price: '))
    profit = sellingPrice - costPrice
    loss = costPrice - sellingPrice

    if costPrice < sellingPrice:
        print('Profit: ', profit)
    else:
        print('Loss: ', loss)

display()