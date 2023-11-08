import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    '''Call the read_compound_list function to read the 
    pupils.csv file into a list named students_list. Write 
    a lambda function that will extract the birthdate from 
    a student. Write a call to the Python built-in sorted 
    function that will sort the students_list by birthdate 
    from oldest to youngest.Print the students_list by calling 
    the print_list function.

    Parameters: none
    Return: nothing
    '''
    students_list = read_compound_list('pupils.csv')

    sorted_list_1 = given_name(students_list)
    print('List Ordered by Given Name')
    print(sorted_list_1)
    print()

    sorted_list_2 = birthdate(students_list)
    print('List Ordered by Birthday')
    print(sorted_list_2)
    print()

    sorted_list_3 = oldest_to_youngest(students_list)
    print('List Ordered by Oldest to Youngest')
    print(sorted_list_3)
    print()


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(list):
    '''takes a list as a parameter and prints each 
    element of the list on a separate line. In other 
    words, this print_list function should include a 
    for loop that prints each element on a separate line.
    
    Parameter
        list: list of items
    Return: the list printed on a seperate line
    '''

    for i in list:
        print(i)
    
    return i

def given_name(student_list):
    '''Sort a list of students by their given name.

    Parameter
        students_list: a list that contains students names,
        and birthdate.
    Return: a new list of students sorted by given name.  
    '''
    students_list = read_compound_list('pupils.csv')

    given_name = lambda student: student[GIVEN_NAME_INDEX]

    sorted_list = sorted(students_list, key = given_name)

    return sorted_list

def birthdate(student_list):
    '''Sort a list of students by their birthday.

    Parameter
        students_list: a list that contains students names,
        and birthdate.
    Return: a new list of students sorted by birthday.  
    '''

    students_list = read_compound_list('pupils.csv')
    def extract_month_and_day(student):
        birthdate = student[BIRTHDATE_INDEX]
        month_and_day = birthdate[5:]

        return month_and_day
    
    sorted_list = sorted(students_list, key = extract_month_and_day)

    return sorted_list

def oldest_to_youngest(students_list):
    '''Sort a list of students from oldest to youngest.

    Parameters
        student_list: a list that contains students names 
        and birthdate.
    Return: a sorted list from oldest to youngest.
    '''

    birthdate = lambda student: student[BIRTHDATE_INDEX]

    sorted_list = sorted(students_list, key = birthdate)

    return sorted_list
# If this file is executed like this:
# > python add_area_code.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()