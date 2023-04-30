def check_entry(entry):
    """Převádí řetězec na celé číslo

    Args:
        entry (str): převáděný řetězec

    Returns:
        result (int): číslo, jinak vyvolá výjimku ValueError
    """
    pass


def is_even(number):
    """Vrací logickou hodnotu určující zda je číslo sudé nebo liché

    Args:
        number (int): testované číslo

    Returns:
        sudost / lichost (bool): Pokud je číslo sudé, vrací True, jinak False.
    """
    pass


def main():
    """Provádění celého programu

    Pro vstup hodnot vypíše "Zadejte celé číslo: " uloží do vstup
    Pokud je číslo sudé vypíše "Zadané číslo je sudé."
    Pokud je číslo liché vypíše "Zadané číslo je liché."
    """
    vstup = ""
    cislo = check_entry(vstup)

    if is_even(cislo):
        pass
    else:
        pass


if __name__ == "__main__":
    main()
