def dynamicky_prumer(cisla):
    suma = 0
    pocet = 0
    prumer = []

    for cislo in cisla:
        suma += cislo
        pocet += 1
        prumer.append(suma / pocet)

    return prumer

if __name__ == "__main__":
    cisla = [1, 2, 3, 4, 5]
    print("Dynamický průměr:", dynamicky_prumer(cisla))
