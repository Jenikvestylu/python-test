def dynamicka_suma():
    suma = 0
    while True:
        cislo = input("Zadejte číslo nebo 'konec' pro ukončení: ")
        if cislo.lower() == 'konec':
            break
        suma += int(cislo)
    return suma

if __name__ == "__main__":
    print("Dynamická suma:", dynamicka_suma())
