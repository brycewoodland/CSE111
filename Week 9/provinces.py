def main():
    """Main function calls the read_list function, removes 
    the first item from list, removes the last item from 
    the list, replaces the AB with Alberta and counts
    the number of Alberta in the list.
    
    Parameters: none
    Return: nothing
    """

    # Read the contents of a text file
    # named plants.txt into a list.
    provinces_list = read_list("provinces.txt")

     # Print the entire list.
    print(provinces_list)

    # Remove the first element from the list.
    provinces_list.pop(0)

    # Remove the last element from the list.
    provinces_list.pop()

    # Replace all occurences of "AB" with "Alberta"
    for i, provinces in enumerate(provinces_list): 
        if provinces_list[i] == 'AB':
            provinces_list[i] = 'Alberta'
    
    print(provinces_list)

    # Count the number of elements that are "Alberta" and print that number.
    amount = provinces_list.count('Alberta')

    print(f'\nAlberta occurs {amount} times in the list.')


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """

    # Create an empty list that will store
    # the lines of text from the text file.
    provinces = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            provinces.append(clean_line)

    # Return the list that contains the lines of text.
    return provinces

# Call main to start this program.
if __name__ == "__main__":
    main()
