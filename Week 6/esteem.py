'''This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.'''


def main():
    score = 0
    score += p_question('1. I feel that I am a person of worth, at least on an equal plane with others.')
    score += p_question ('2. I feel that I have a number of good qualities.')
    score += n_question ('3. All in all, I am inclined to feel that I am a failure.')
    score += p_question ('4. I am able to do things as well as most other people.')
    score += n_question ('5. I feel I do not have much to be proud of.')
    score += p_question ('6. I take a positive attitude toward myself.')
    score += p_question ('7. On the whole, I am satisfied with myself.')
    score += n_question ('8. I wish I could have more respect for myself.')
    score += n_question ('9. I certainly feel useless at times.')
    score += n_question ('10. At times I think I am no good at all.')

    print()
    print(f'Your score is {score}.')
    print("A score below 15 may indicate probelmatic low self-esteem.")

def p_question(question):
    '''Display one statement to the user and get the user's response then determine the score for the response and return the score. 
    
    Parameters
        question: The question to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score for the user'''
    
    print(question)
    answer = input('Enter D, d, a, or A: ')
    if answer == 'D':
        score = 0 
    elif answer == 'd':
        score = 1
    elif answer == 'a':
        score = 2
    else:
        score = 3
    return score
    

def n_question(question):
    '''Display one statement to the user and get the user's response then determine the score for the response and return the score. 
    
    Parameters
        question: The question to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score for the user'''
    
    print(question)
    answer = input('Enter D, d, a, or A: ')
    if answer == 'D':
        score = 3 
    elif answer == 'd':
        score = 2
    elif answer == 'a':
        score = 1
    else:
        score = 0
    return score

if __name__ == "__main__":
    main()

    
    
