import pytest
import sude_cislo


def test_is_even():
    assert sude_cislo.is_even(4)
    assert not sude_cislo.is_even(5)
    assert sude_cislo.is_even(0)
    assert sude_cislo.is_even(-4)
    assert not sude_cislo.is_even(-5)


def test_check_entry():
    assert sude_cislo.check_entry("1234") == 1234
    with pytest.raises(ValueError, match="Zadaná hodnota není číslo."):
        sude_cislo.check_entry("cokoliv")
