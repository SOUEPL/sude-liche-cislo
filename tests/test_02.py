# Do not edit these lines
import sys
sys.path.insert(0, "./")  # Adds higher directory to python modules path.
import sude_cislo


def test_is_even():
    assert sude_cislo.is_even(4)
    assert not sude_cislo.is_even(5)
    assert sude_cislo.is_even(0)
