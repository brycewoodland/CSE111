'''
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. The second number is the aspect ratio. The 
third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a 
tire can be approximated with this formula:

v = pi * w^2 * a (w * a + 2,540 * d) / 10,000,000,000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
'''

import math

def volume(w, r, d): # <-- Parameters 
    return (math.pi * w ** 2 * r * (w * r + 2540 * d)) / 10000000000

w = int(input('Enter the width of the tire in mm (ex 205): ')) # 205
a = int(input('Enter the aspect ratio of the tire (ex 60): ')) # 60
d = int(input('Enter the diameter of the wheel in inches (ex 15): ')) # 15

v = volume(w, a, d) # <-- Arguments
print(f'\n{v:.2f}')
