#menu

print("Witaj w programie losującym!")
print("Wybierz jedną z opcji")
print("1.Randomizer z liczba minimalna oraz maksymalna")
print("2.Rzut koscmi")
print("3.Orzeł czy reszka")
print("4.Wylacz")
x = (input("1/2/3/4?:"))
while True:
    if x in ('1','2','3','4'):
        if x == "1":
            import randomizer
        elif x == "2":
            import kosci
        elif x == "3":
            import reszka
        elif x == "4":
            import wylacz
        break
    else:
        input("Blad! Nie ma takiej opcji, nacisnij dowolny klawisz aby kontynuowac.")
        import main
    

