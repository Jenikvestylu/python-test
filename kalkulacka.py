def kalkulacka():
    operace = input("Vyberte operaci (+, -, *, /): ")
    cislo1 = float(input("Zadejte první číslo: "))
    cislo2 = float(input("Zadejte druhé číslo: "))

    if operace == '+':
        return cislo1 + cislo2
    elif operace == '-':
        return cislo1 - cislo2
    elif operace == '*':
        return cislo1 * cislo2
    elif operace == '/':
        if cislo2 != 0:
            return cislo1 / cislo2
        else:
            return "Chyba: Nelze dělit nulou."
    else:
        return "Chyba: Neplatná operace."

if __name__ == "__main__":
    print("Výsledek kalkulačky:", kalkulacka())
