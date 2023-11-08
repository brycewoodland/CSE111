'''
Author: Bryce Woodland

A program that allows a user to play the game: 'rock, paper, and scissors'
'''
import random

actions = ['rock', 'paper', 'scissors']

# dictionary for available actions with game results
victories = {'rock':      (actions[0], actions[2]),
             'paper':     (actions[1], actions[0]),
             'scissors':  (actions[2], actions[1])
            }
  
def main():
    """Call the user_choice function to get an input. Call
    the get_computer_choice function to randomly choose an
    input. Call decide_winner function to decide who wins.
    
    Parameters: none
    Return: nothing
    """
    while True:
        try:
            print('\nRock, Paper, Scissors - Shoot!\n')

            # call user_choice and assign it a variable
            user_choice = get_user_choice()
        
            # call computer_choice and assign it a variable
            computer_choice = get_computer_choice()

            # call decide_winner and input arguments
            decide_winner(user_choice, computer_choice)
            print()

            play_more = input('Do you want to play again? (y/n) ')
            if play_more.lower() != 'y':
                break

        except KeyError as key_err:
            print()
            print(f'Invalid selection: {key_err}. Please choose rock, paper, or scissors.')

def get_user_choice():
    """Have the user input a choice between rock, paper
    and scissors. Display their choice and return their
    decision.

    Parameters: none
    Return: the decision of the user
    """

    # input statement for user to enter a choice (rock, paper, scissors)
    user_choice = input('Enter a choice to start the game: ').lower()
    print()
    
    # print out their decision and make sure it's valid
    print(f'Your choice: {user_choice}')

    return user_choice

def get_computer_choice():
    """Get a random choice of rock, paper, and scissors 
    to compare with the users choice. Print the computer's
    random choice. Return their decision. 
    
    Parameter: none
    Return: the random decision of the computer
    """

    # Have the computer choose a random action
    program_choice = random.choice(actions)

    # display the computer's decision
    print(f'Computer choice: {program_choice}')

    return program_choice

def decide_winner(user_choice, computer_choice):
    """Compare the choices between the user and the computer.
    If they are the same == tie. If they are different display
    who wins.
    
    Parameters
        user_choice: the decision the user went with
        computer_choice: the random decision of the computer
    Return: nothing
    """
    defeats = victories[user_choice]

    if user_choice == computer_choice:
        print('You tie!')
    elif computer_choice in defeats:
        print('You win!')
    else:
        print('You lose!')
    
# Call the main function
if __name__ == "__main__":
    main()
