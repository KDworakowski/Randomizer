#reszka

import random

random_again = "t"

while random_again == "t":
    if random_again == "t":
        print("Losuje...")
        print("Wylosowana liczba to:", random.randint(1, 2))
        random_again = input("Losowac ponownie? (t/n):")
    if random_again == "n":
        quit = input("Czy napewno chesz wrocic do menu? (t/n):")
    if quit == "t":
            print("Ok!")
            import main
    if quit == "n":
        random_again = input("Losowac ponownie? (t/n):")
pass