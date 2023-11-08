"""
Author: Bryce Woodland

A common task for many knowledge workers is to use a number, key, or ID to find 
information about a person. For example, a knowledge worker may use a phone number or 
e-mail address as a key to find (or look up) additional information about a customer. 
During this activity, your team will write a Python program that uses a student’s 
I-Number to look up the student’s name.
"""
import csv

# Indexes of the columns
# in the students.csv file.
INUMBER_INDEX = 0
NAME_INDEX = 1

def main():
    """Get an I-Number from the user, use the 
    I-Number to find the corresponding student 
    name in the dictionary, and print the name.

    Parameters: 
        i_number: get an i number from the user
    Return: the name of the student that corresponds
    with the I number
    """
    # Read the contents of a CSV file named students.csv
    # into a dictionary named students_dict. Use the I-Number
    # as the key in the dictionary.
    students_dict = read_dictionary('students.csv', INUMBER_INDEX)

    # Get an I-Number from the user
    i_number = input('What is the I-Number? ')

    # If a user enters an I-Number that doesn’t exist 
    # in the dictionary, your program must print the 
    # message, "No such student" (without the quotes
        # Determine if the user input is formatted correctly.
    if not i_number.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(i_number) < 9:
            print("Invalid I-Number: too few digits")
        elif len(i_number) > 9:
            print("Invalid I-Number: too many digits")
        else:
            # The user input is a valid I-Number. Find
            # the I-Number in the list of I-Numbers.
            if i_number not in students_dict:
                print("No such student")
            else:
                # Retrieve the student name that corresponds
                # to the I-Number that the user entered.
                value = students_dict[i_number]
                name = value[NAME_INDEX]

                # print the name
                print(name)


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """

    # Create an empty list that will store
    # the lines of text from the text file.
    text_dict = {}

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the contents of the text
        # file one line at a time.
        for row in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row[key_column_index]

            # Store the data from the current
            # row into the dictionary.
            text_dict[key] = row

    # Return the list that contains the lines of text.
    return text_dict

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()