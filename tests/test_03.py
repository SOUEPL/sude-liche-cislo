# Do not edit these lines

import sys
import pytest
sys.path.append(".")  # Adds higher directory to python modules path.
import sude_cislo


def test_check_entry():
    assert sude_cislo.check_entry("1234") == 1234
    with pytest.raises(ValueError, match="Zadaná hodnota není číslo."):
        sude_cislo.check_entry("cokoliv")
