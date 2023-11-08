"""
Author: Bryce Woodland

Program to test rock_paper_scissors.py and make sure the functions 
are working properly.
"""
import pytest

from rock_paper_scissors import decide_winner

def test_get_user_choice_1(monkeypatch):
    """Verify that the get_user_choice()
    function works as it should.
    
    Parameters: none
    Return: nothing
    """
    monkeypatch.setattr('builtins.input', lambda _: 'rock')

    i = input('Enter a choice: ')
    assert i == 'rock'

def test_get_user_choice_2(monkeypatch):
    """Verify that the get_user_choice()
    function works as it should.
    
    Parameters: none
    Return: nothing
    """
    monkeypatch.setattr('builtins.input', lambda _: 'paper')

    i = input('Enter a choice: ')
    assert i == 'paper'

def test_get_user_choice_3(monkeypatch):
    """Verify that the get_user_choice()
    function works as it should.
    
    Parameters: none
    Return: nothing
    """
    monkeypatch.setattr('builtins.input', lambda _: 'scissors')

    i = input('Enter a choice: ')
    assert i == 'scissors'

def test_decide_winner():
    """Verify that the decide_winner()
    function works as it should
    
    Parameters: none
    Return: nothing
    """
    assert decide_winner('rock', 'rock') == print('You tie!')
    assert decide_winner('paper', 'paper') == print('You tie!')
    assert decide_winner('scissors', 'scissors') == print('You tie!')
    assert decide_winner('rock', 'scissors') == print('You win!')
    assert decide_winner('scissors', 'paper') == print('You win!')
    assert decide_winner('paper', 'rock') == print('You win!')
    assert decide_winner('scissors', 'rock') == print('You lose!')
    assert decide_winner('paper', 'scissors') == print('You lose!')
    assert decide_winner('rock', 'paper') == print('You lose!')

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
