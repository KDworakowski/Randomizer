#ranodmizer

import random
min = int(input("Podaj liczbe minimalna:"))
max = int(input("Podaj liczbe maksymalna:"))

random_again = "tak"

while random_again == "tak" or random_again == "t":
    if random_again == "tak" or "t":
        print("Losuje...")
        print("Wylosowana liczba to:", random.randint(min, max))
        random_again = input("Losowac ponownie?:")
        if random_again != "tak" or "t":
            print("Dzieki!")
            pass