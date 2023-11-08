# names = ['A', 'B', 'C', 'D', 'E']

# surname = 'Keers'

# print(names)

# def change(lst):
#     for i, name in enumerate(lst): 
#         names[i] = names[i] + ' ' + surname

# change(names)

# print(names)

numbers = [1, 2, 3, 4]

def do_something(nums, funcs):
    for i, num in enumerate(nums):
        for func in funcs:
            nums[i] = func(nums[i])

def add_ten(num):
    return num + 100

def far_to_cels(num):
    return (num -32) * 5 / 9

def multiple_by_five(num):
    return num * 5

do_something(numbers, [add_ten, multiple_by_five, far_to_cels])

print(numbers)