def check_entry(a):
    try:
        result = int(a)
    except ValueError:
        raise ValueError("Zadaná hodnota není číslo.")
    return result


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


vstup = "100"
cislo = check_entry(vstup)

if is_even(cislo):
    print("Zadané číslo je sudé.")
else:
    print("Zadané číslo je liché.")
