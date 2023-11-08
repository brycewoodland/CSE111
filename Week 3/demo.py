def main():
    """
    ...
    """
    # Gather user input...
    y = input('What would you like to yell? ')
    w = input('What would you like to whisper? ')
    d = input('What would you like to day dream about? ')

    # Print results to the user.
    print(yell(y))
    print(whisper(w))
    print(day_dreaming(d))

def day_dreaming(sentence):
    """
    ...
    """
    return f'*{sentence}*'

def yell(sentence):
    """
    ...
    """
    return sentence.upper()

def whisper(sentence):
    
    """
    Lowercase a sentence

    Parameters: 
    sentence (str): The sentence to lowercase

    Returns:
    str: The sentence that has been lowercased. 
    """
    return sentence.lower()

main()