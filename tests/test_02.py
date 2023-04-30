# Do not edit these lines
import sys
sys.path.insert(0, "./")  # Adds higher directory to python modules path.
from main import *


def test_is_even():
    assert is_even(4)
    assert not is_even(5)
    assert is_even(0)
