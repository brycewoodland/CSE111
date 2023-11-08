'''
You work for a retail store that wants to increase sales on Tuesday and Wednesday, 
which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s 
subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.
'''

from datetime import datetime

discount = 0.10
sales_tax = 0.06

subtotal = float(input('Please enter the subtotal: '))

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday() 

if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = round(subtotal * discount, 2)
    print(f'Discount amount: {discount:.2f}')
    subtotal -= discount

sales_tax = round(subtotal * sales_tax, 2)
print(f'Sales tax amount: {sales_tax:.2f}')

total = subtotal + sales_tax
print(f'Total: {total:.2f}')