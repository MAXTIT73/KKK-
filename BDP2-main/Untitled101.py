lista_zapupów = {
    "banany": {"ilość": "1"},
    "apple": {"ilość": "8"},
    "onion": {"ilość": "4"},
    "milk": {"ilość": "3"},
    "meat": {"ilość": "2"},
}
while True:
    print("\n---Lista Zakupów---")
    print("dodać product - a")
    print("usunąć product - b")
    print("sprawdzicz dostępność produktu - c")
    print("wyswietlić wszystko - d")

    wybor = input("wpisz a/b/c/d: ")

    if wybor == "a":
        j = input("wpisz nazwe: ")
        f = int(input("wpisz ilość:"))
        lista_zapupów[j] = {"ilość": f}

    elif wybor == "b":
        t = input("wpisz nazwe: ")
        if t in lista_zapupów:
            del lista_zapupów[t]
        else:
            print("nie ma tego produktu")

    elif wybor == "c":
        v = input("Podaj nazwę produktu: ")

        if v in lista_zapupów:
            print(f"Produkt '{v}' jest dostępny: {lista_zapupów[v]['ilość']} szt.")
        else:
            print("Produkt niedostępny")

    elif wybor == "d":
        if lista_zapupów:
            print("\n--- Produkty w magazynie ---")
            for nazwa, dane in lista_zapupów.items():
                print(f"{nazwa} - {dane['ilość']} szt.")
        else:
            print("lista jest pusta")