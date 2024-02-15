def je_sude(cislo):
    return cislo % 2 == 0

if __name__ == "__main__":
    cislo = int(input("Zadejte číslo pro ověření sudosti: "))
    if je_sude(cislo):
        print("Číslo je sudé.")
    else:
        print("Číslo není sudé.")
