# Do not edit these lines
import sys
import pytest
sys.path.insert(0, "./")  # Adds higher directory to python modules path.
from main import *


def test_check_entry():
    assert check_entry("1234") == 1234
    with pytest.raises(ValueError, match="Zadaná hodnota není číslo."):
        check_entry("cokoliv")
