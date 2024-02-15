def pocet_sudych_cisel(seznam):
    pocet = 0
    for cislo in seznam:
        if cislo % 2 == 0:
            pocet += 1
    return pocet

if __name__ == "__main__":
    seznam_cisel = [5, 3, 8, 1, 9, 12, 15]
    print("Počet sudých čísel v poli:", pocet_sudych_cisel(seznam_cisel))
