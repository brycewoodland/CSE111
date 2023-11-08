from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that make_full_name function works properly.
    Parameters: none
    Return: nothing
    """
    assert make_full_name("Brown", "Sally") == "Brown; Sally"
    assert make_full_name("Woodland", "Bryce") == "Woodland; Bryce"
    assert make_full_name("Keers", "Christopher David") == "Keers; Christopher David"

def test_extract_family_name():
    """Verify that extract_family_name function works properly.
    Parameters: none
    Return: nothing
    """
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Woodland; Bryce") == "Woodland"
    assert extract_family_name("Keers; Christopher David") == "Keers"

def test_extract_given_name():
    """Verify that extract_given_name function works properly.
    Paramters: none
    Return: nothing
    """
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Woodland; Bryce") == "Bryce"
    assert extract_given_name("Keers; Christopher David") == "Christopher David"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])