''' 
Author: Bryce Woodland

Prove that you can write functions with parameters and call those functions multiple times with arguments.
'''

import random

def main():
    """Call the make_sentence function 6 times to print
    and display 3 singular sentences with differing 
    tenses (Past, Present, Future) and 3 plural sentences 
    with differing tenses (Past, Present, Future).
    """

    single_past_sentence = make_sentence(quantity=1, tense='past')
    single_present_sentence = make_sentence(quantity=1, tense='present')
    single_future_sentence = make_sentence(quantity=1, tense='future')
    plural_past_sentence = make_sentence(quantity=2, tense='past')
    plural_present_sentence = make_sentence(quantity=2, tense='present')
    plural_future_sentence = make_sentence(quantity=2, tense='future')

    print(single_past_sentence)
    print(single_present_sentence)
    print(single_future_sentence)
    print(plural_past_sentence)
    print(plural_present_sentence)
    print(plural_future_sentence)

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """

    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    if quantity == 1:
        words = ['bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man', 'rabbit', 'woman']
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    # Randomly choose and return a determiner.
    noun = random.choice(words)
    
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == 'past':
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present' and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 'present' and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]

    #Randomly choose and return a verb
    verb = random.choice(words)
    
    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # Randomly choose and return a preposition
    preposition = random.choice(words)
    
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or plural.
    Return: a prepositional phrase.
    """

    # build a prepositional phrase
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    
    return f'{preposition} {determiner} {noun}'

def get_adjective():
    '''Return a randomly chosen adjective from this
    list of adjectives:
        ['silly', 'bald', 'beautiful', 'cheesy', 'faithful',
        'gentle', 'happy', 'jolly', 'nice', 'grumpy']
        '''
    words = ['silly', 'bald', 'beautiful', 'cheesy', 'faithful',
        'gentle', 'happy', 'jolly', 'nice', 'grumpy', 'red', 'busy',
        'dinky']
    
    # Randomly choose and return an adjective
    adjective = random.choice(words)

    return adjective

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    # Builds a sentence by calling previous functions and setting them to a variable
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    adjective = get_adjective()
    prepositional_phrase = get_prepositional_phrase(quantity)
    
    return f'{determiner.capitalize()} {adjective} {noun} {prepositional_phrase} {verb}.'

main()