'''
Author: Bryce Woodland

Improve your ability to write object-oriented code.
'''

def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # Add code to reverse and print fruit_list.
    fruit_list.reverse()
    print(f'Reversed: {fruit_list}')

    # Add code to append "orange" to the end of 
    # fruit_list and print the list.
    fruit_list.append('orange')
    print(f'List w/orange: {fruit_list}')

    # Add code to find where "apple" is located in 
    # fruit_list and insert "cherry" before "apple" 
    # in the list and print the list.
    index = fruit_list.index('apple')
    fruit_list.insert(index, 'cherry')
    print(f'List w/cherry: {fruit_list}')

    # Add code to remove "banana" from fruit_list 
    # and print the list.
    fruit_list.remove('banana')
    print(f'List without banana: {fruit_list}')

    # Add code to pop the last element from fruit_list 
    # and print the popped element and the list.
    fruit_list.pop()
    print(f'Pop last item: {fruit_list}')

    # Add code to sort and print fruit_list.
    fruit_list.sort()
    print(f'Sorted: {fruit_list}')

    # Add code to clear and print fruit_list.
    fruit_list.clear()
    print(f'Clear: {fruit_list}')

if __name__ == '__main__':
    main()
          