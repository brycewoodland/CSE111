# def family(surname, *names): # <-- Parameters?, function signature
#     for name in names:
#         print(f'{name} {surname}')

#     '''
#     Explain what this does in a single line

#     Long explanation if needed...

#     Parameters: 
#     a (str): This is the first positional argument.
#     b (str): This is the second positional argument.
#     '''

# # Positional arguments

# # [] list <-- array
# # [] tuple (immutable)

# family('Woodland', 'Megan', 'Amy', 'Mallory') 

def person(**names):
    print(f"{names['fname']} {names['mname']} {names['lname']}")

person(fname='Christopher', mname='David', lname='Keers', age='', address='')