"""
Author: Bryce Woodland

Many companies wish to understand the needs and wants of their customers more deeply so the company can create 
products that fill those needs and wants. One way to understand customers more deeply is to record the values 
entered by customers while they are using a program and then to analyze those values. One common way to record 
values is for a program to store them in a file
"""

import math
from datetime import datetime

current_date_and_time = datetime.now()

def volume(w, r, d): # <-- Parameters 
    return (math.pi * w ** 2 * r * (w * r + 2540 * d)) / 10000000000

w = int(input('Enter the width of the tire in mm (ex 205): ')) # 205
a = int(input('Enter the aspect ratio of the tire (ex 60): ')) # 60
d = int(input('Enter the diameter of the wheel in inches (ex 15): ')) # 15

v = volume(w, a, d) # <-- Arguments
print(f'\nThe approximate volume is {v:.2f} liters')

# If statements to determine the price of the customer's tires
if w <= 185 and a <= 50 and d <= 14:
    print('The price of tire is $50.12.')
elif w <= 205 and a <= 60 and d <= 15:
    print('The price of tire is $70.59.')
elif w <= 225 and a <= 70 and d <= 16:
    print('The price of tire is $101.99. ')
else:
    print('The price of tire is $125.62.')

# Input statement that asks user if they would like to purchase tires
buy_or_not = input('Would you like to purchase new tires? ')

# If/else statements that depend upon whether the customer wants
# to purchase new tires or not
if buy_or_not == 'yes'.lower():
    phone_number = input('What is your phone number? ') # asks user for their phone number to store in file
    with open('volumes.txt', 'at') as volumes_file:
        print(f'{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, {phone_number}', file=volumes_file) 
else:
    with open('volumes.txt', 'at') as volumes_file:
        print(f'{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}', file=volumes_file)