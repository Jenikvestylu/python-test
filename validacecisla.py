def validace_telefonniho_cisla(cislo):
    if len(cislo) == 9:
        return True
    elif len(cislo) == 13 and cislo.startswith('+'):
        return True
    else:
        return False

if __name__ == "__main__":
    cislo_telefonu = input("Zadejte telefonní číslo pro validaci: ")
    if validace_telefonniho_cisla(cislo_telefonu):
        print("Telefonní číslo je platné.")
    else:
        print("Telefonní číslo není platné.")
