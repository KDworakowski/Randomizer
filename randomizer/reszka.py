#reszka

import random

random_again = "tak"

while random_again == "tak" or random_again == "t":
    if random_again == "tak" or "t":
        print("Losuje...")
        print("Wylosowana liczba to:", random.randint(1, 2))
        random_again = input("Losowac ponownie? (t/n):")
    if random_again != "tak" or "t":
        x = input("Czy napewno chcesz wrocic do menu? (t/n):")
        if x == "tak" or x == "t":
            print("Ok!")
            import main
pass