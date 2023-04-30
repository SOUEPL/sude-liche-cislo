# Do not edit these lines

from io_test import set_keyboard_input, get_display_output
import sys
sys.path.append(".")  # Adds higher directory to python modules path.
import sude_cislo


def test_io():
    set_keyboard_input(["1234"])
    sude_cislo.main()
    output = get_display_output()
    assert output == ["Zadejte celé číslo: ", "Zadané číslo je sudé."]
