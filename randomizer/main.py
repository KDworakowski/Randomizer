#menu

print("Witaj w programie losującym!")
print("Wybierz jedną z opcji")
print("1.Randomizer z liczba minimalna oraz maksymalna")
print("2.Rzut koscmi")
print("3.Orzeł czy reszka")
print("4.Wylacz")
x = int(input("1/2/3/4?:"))

while x == 1:
    import randomizer
pass

while x == 2:
    import kosci
pass

while x == 3:
    import reszka
pass

while x == 4:
    print("Czy napewno chcesz wylaczyc?")
    y = input("t/n?:")
    if y == "t":
        break
    if y == "n":
        import main
else:
    input("Blad! Nie ma takiej opcji, nacisnij dowolny klawisz aby kontynuowac.")
    import main