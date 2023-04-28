import prvni_pokus
import pytest


def test_is_even():
    assert prvni_pokus.is_even(4)
    assert not prvni_pokus.is_even(5)
    assert prvni_pokus.is_even(0)
    assert prvni_pokus.is_even(-4)
    assert not prvni_pokus.is_even(-5)


def test_check_entry():
    assert prvni_pokus.check_entry("1234") == 1234
    with pytest.raises(ValueError, match="Zadaná hodnota není číslo."):
        prvni_pokus.check_entry("cokoliv")
