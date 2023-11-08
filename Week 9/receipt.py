"""
Author: Bryce Woodland

A local grocery store subscribes to an online service 
that enables its customers to order groceries online. 
After a customer completes an order, the online service 
sends a CSV file that contains the customer’s requests to 
the grocery store. The store needs you to write a program 
that reads the CSV file and prints to the terminal window 
a receipt that lists the purchased items and shows the subtotal, 
the sales tax amount, and the total.
"""
import csv

# Indexes from the request.csv file
PRODUCT_NUMBER_INDEX = 0
QUANTITY_INDEX = 1

# Indexes from the products.csv 
PRODUCT_NAME = 1
PRODUCT_PRICE_INDEX = 2

def main():
    """Call the read_dictionary function and store compound dict
    in a variable called products_dict. Print the products_dict.
    Open the request.csv file for reading. Skip the first line
    in request.csv. Use a loop that reads each row.

    Parameters: none
    Return: nothing
    """

    # Calls the read_dictionary function and stores the 
    # compound dictionary in a variable named products_dict.
    products_dict = read_dictionary('products.csv', PRODUCT_NUMBER_INDEX) 

    # Prints the products_dict.
    print(f'All Products \n {products_dict}')
    print()

    # Opens the request.csv file for reading.
    with open ('request.csv', 'rt') as request_file:

         # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(request_file)

        # The first row of the CSV file contains column
        # headings and not data about a dental office,
        # so this statement skips the first row of the
        # CSV file.
        next(reader, None)

        # Read each row in the CSV file one at a time.
        # The reader object returns each row as a list.
        print('Requested Items')
        for row_list in reader:

            product_number_key = row_list[PRODUCT_NUMBER_INDEX]

            product_name = products_dict[product_number_key][PRODUCT_NAME]
            quantity = row_list[QUANTITY_INDEX]
            product_price = products_dict[product_number_key][PRODUCT_PRICE_INDEX]
            
            # Print the product name, requested quantity, and product price.
            print(f'{product_name}: {quantity} @ {product_price}')

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

        # Create an empty list that will store
    # the lines of text from the text file.
    compound_dict = {}

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, 'rt') as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader, None)

        # Read the contents of the text
        # file one line at a time.
        for row_list in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]

            # Store the data from the current
            # row into the dictionary.
            compound_dict[key] = row_list

    # Return the list that contains the lines of text.
    return compound_dict

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()