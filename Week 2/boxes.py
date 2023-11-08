'''
In our modern world economy, many items are manufactured in 
large factories, then packed in boxes and shipped to 
distribution centers and retail stores. A common question 
for employees who pack items is “How many boxes do we need?”

A manufacturing company needs a program that will help its employees 
pack manufactured items into boxes for shipping. Write a Python program 
named boxes.py that asks the user for two integers:

1. the number of manufactured items
2. the number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to 
hold the items. This must be a whole number. Note that the last box may 
be packed with fewer items than the other boxes.
'''
# Allows the import of math.ceil
import math

# Variables 
number_manufactured_items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

# Calculation that needs to be performed for number of boxes needed
calculation = math.ceil(number_manufactured_items / items_per_box)

# Output or Result
print(f'\nFor {number_manufactured_items} items, packing {items_per_box} items in each box, you will need {calculation} boxes.')