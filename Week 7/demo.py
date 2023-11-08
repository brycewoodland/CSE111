from array import array

numbers = array('i')

while len(numbers) < 5:
    num = input('Favorite number: ')
    try:
        num = int(num)
    except:
        print('Please enter only a whole number!')
        continue
    numbers.append(num)

for i, num in enumerate(numbers):
    print(f'{i + 1}) {num}')