from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    """Verify that extract_city function works properly.
    Parameters: none
    Return: nothing
    """
    assert extract_city("123 Crazy Lane, Rexburg, Idaho 84430") == "Rexburg"
    assert extract_city("123 Crazy Lane, Murray, Utah 84123") == "Murray"

def test_extract_state():
    """Verify that extract_state function works properly.
    Parameters: none
    Return: nothing
    """
    assert extract_state("123 Crazy Lane, Rexburg, Idaho 84430") == "Idaho"
    assert extract_state("123 Crazy Lane, Murray, Utah 84123") == "Utah"

def test_extract_zipcode():
    """Verify that extract_zipcode works properly.
    Parameters: none
    Return: nothing
    """
    assert extract_zipcode("123 Crazy Lane, Rexburg, Idaho 84430") == "84430"
    assert extract_zipcode("123 Crazy Lane, Murray, Utah 84123") == "84123"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])