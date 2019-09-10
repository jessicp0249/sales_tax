# File: main.py
# Description: Program will prompt user for a purchase subtotal, calculate tax, 
# and print a receipt with the subtotal, taxes, and total.
# Author: Jessica Priester
# Email: jessicp0249@student.vvc.edu
# Date created: 10 Sep 2019

# Tax rates
state_tax_rate = 0.05
sales_tax_rate = 0.025

# Get subtotal from user
subtotal = float(input('Please enter your purchase subtotal:\n'))

# Calculate taxes and final total
state_tax = state_tax_rate * subtotal
sales_tax = sales_tax_rate * subtotal
total = subtotal + state_tax + sales_tax

# Print receipt
print('Subtotal: $%0.2f' % (subtotal))
print('State tax: $%0.4f' % (state_tax))
print('County sales tax: $%0.4f' % (sales_tax))
print('Total tax: $%0.4f' % (state_tax + sales_tax))
print('Total cost: $%0.2f' % (total))
