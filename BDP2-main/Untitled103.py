rowery = [
    {"id": 1, "model": "Cross", "typ": "MTB", "cena": 10.5, "dostepny": False},
    {"id": 2, "model": "big", "typ": "Trekking", "cena": 12.5, "dostepny": True},
    {"id": 3, "model": "circle", "typ": "Szosa", "cena": 18.0, "dostepny": True},
    {"id": 4, "model": "Scott", "typ": "MTB", "cena": 8.0, "dostepny": False},
    {"id": 5, "model": "Merida", "typ": "Cross", "cena": 12.4, "dostepny": False}
]

def zpID(lista, szukane_id):
    for FA in lista:
        if FA["id"] == szukane_id:
            return FA
    return None


while True:
    print("\n--- MENU ---")
    print("1. Wszystkie rowery")
    print("2. Dostępne rowery")
    print("3. Wypożycz")
    print("4. Oddaj")
    print("5. Koszt wypożyczenia")
    print("6. Najtańszy i najdroższy")
    print("B. Wyjście")

    wybor = input("Opcja: ")

    if wybor == "1":
        for FA in rowery:
            print(FA)

    elif wybor == "2":
        for FA in rowery:
            if FA["dostepny"]:
                print(FA)

    elif wybor == "3":
        FA = zpID(rowery, int(input("ID: ")))
        if FA and FA["dostepny"]:
            FA["dostepny"] = False
            print("Wypożyczono:", FA["model"])
        else:
            print("Nie można wypożyczyć.")

    elif wybor == "4":
        FA = zpID(rowery, int(input("ID: ")))
        if FA and not FA["dostępny"]:
            FA["dostepny"] = True
            print("Oddano", FA["model"])
        else:
            print("Nie można oddać. ")

    elif wybor == "5":
        G = int(input("Ilosz godzin: "))
        print(G*["cena"])

    elif wybor == "6":
        for FA in rowery:
            if FA = max(rowery):
                print(FA)
            elif FA = min(rowery):
                print(FA)
            else:
                pass            
    
    elif wybor == "B":
        break

    else:
        print("Prestań pisać cokolwiek przyjdzie ci do głowy!! Czytaj Menu!!🤬🤬")