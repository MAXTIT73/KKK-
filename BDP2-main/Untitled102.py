kA = {
    "kapucyńska": {"20": "Ania"},
    "Konopnica": {"254B": "Alex"},
    "Diamentowa": {"2C": "Olivia"},
    "Onyksowa": {"9B": "Maksym"},
    "Dolna_Pani_Marii": {"14": "Andrzej"},
}
while True:
    print("\n---Książka adresowa---")
    print("dodać adres - a")
    print("usunąć adres - b")
    print("sprawdzicz dostępność adresu - c")
    print("wyswietlić wszystko - d")

    wybor = input("wpisz a/b/c/d: ")

    if wybor == "a":
        j = input("wpisz ulice: ")
        f = int(input("wpisz numer:"))
        kA[j] = {"numer": f}

    elif wybor == "b":
        t = input("wpisz ulice: ")
        if t in kA:
            del kA[t]
        else:
            print("nie ma tego produktu")

    elif wybor == "c":
        v = input("Podaj ulice: ")

        if v in kA:
            print(f"adres '{v}' jest dostępny: {kA[v]['numer']}")
        else:
            print("Produkt niedostępny")

    elif wybor == "d": 
       print("\n--- WSZYSTKIE KONTAKTY ---") 
       for k, osoby in kA.items(): 
           print(f"\n[{k}]") 
           for imie, tel in osoby.items(): 
               print(f" - {imie}: {tel}")