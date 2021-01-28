#ranodmizer

import random
min = int(input("Podaj liczbe minimalna:"))
max = int(input("Podaj liczbe maksymalna:"))

random_again = "t"

while random_again == "t":
    if random_again == "t":
        print("Losuje...")
        print("Wylosowana liczba to:", random.randint(min, max))
        random_again = input("Losowac ponownie? (t/n):")
    if random_again == "n":
        quit = input("Czy napewno chesz wrocic do menu? (t/n):")
    if quit == "t":
            print("Ok!")
            import main
    if quit == "n":
        import randomizer
pass