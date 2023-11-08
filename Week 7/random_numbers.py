'''
Author: Bryce Woodland

There are a few details about writing and calling functions in Python that, if you understand, will
 help you be a more effective programmer. These details include default parameter values and 
 pass by reference. As a team during this activity, you will write and call a function that demonstrates 
 both default parameter values and pass by reference.
'''

import random

def main():
    """
    Creates a list of numbers and prints that list. Calls the append_random_numbers 
    function with one argument and prints the list with the new number. 
    Calls the append_random_numbers function with two arguments and prints the new list.

    Parameters: none
    Return: nothing 
    """
    numbers = [16.2, 75.1, 52.3]
    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)

    words = []
    
    append_random_words(words)
    print(words)

    append_random_words(words, 3)
    print(words)


def append_random_numbers(numbers_list, quantity=1):
    """
    Appends random numbers to the numbers list. Computes the quantity by calling 
    the random.uniform function. Rounds the random numbers to one digit
    after the decimal. 

    Parameters
        numbers_list: the list of numbers
        quantity:
    Return: nothing 
    """
    for i in range(quantity):
        random_number = random.uniform(0, 100)
        rounded_random_number = round(random_number, 1)
        numbers_list.append(rounded_random_number)

def append_random_words(words_list, quantity=1):
    """
    Appends a random word to a the word_list by selecting from a random list.

    Parameters
        words_list: the list of words
        quantity: the amount of words wanted 
    Return: nothing
    """
    options = ['heart', 'head', 'car', 'wagon', 'list',
               'kiss', 'laugh', 'love', 'swim', 'run', 
               'dance', 'drive', 'jump', 'crash']

    for i in range(quantity):
        random_word = random.choice(options)
        words_list.append(random_word)

if __name__ == "__main__":
    main()