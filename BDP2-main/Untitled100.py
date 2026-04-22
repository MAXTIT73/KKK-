sklep = {
    "banana": {"ilość": "320"},
    "apple": {"ilość": "235"},
    "onion": {"ilość": "120"},
    "milk": {"ilość": "610"},
    "meat": {"ilość": "238"},
}
while True:
    print("\n---Sklep Internetowy---")
    print("---MENU---")
    print("dodać product - 1")
    print("usunąć product - 2")
    print("sprawdzicz dostępność produktu - 3")
    print("wyswietlić wszystko - 4")

    wybor = input("wpisz 1/2/3/4: ")

    if wybor == "1":
        j = input("wpisz nazwe: ")
        f = int(input("wpisz ilość:"))
        sklep[j] = {"ilość": f}

    elif wybor == "2":
        t = input("wpisz nazwe: ")
        if t in sklep:
            del sklep[t]
        else:
            print("nie ma tego produktu")

    elif wybor == "3":
        v = input("Podaj nazwę produktu: ")

        if v in sklep:
            print(f"Produkt '{v}' jest dostępny: {sklep[v]['ilość']} szt.")
        else:
            print("Produkt niedostępny")

    elif wybor == "4":
        if sklep:
            print("\n--- Produkty w magazynie ---")
            for nazwa, dane in sklep.items():
                print(f"{nazwa} - {dane['ilość']} szt.")
        else:
            print("Magazyn jest pusty")