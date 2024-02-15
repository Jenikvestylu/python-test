def prevod_sekund(cas):
    dny = cas // 86400
    cas %= 86400
    hodiny = cas // 3600
    cas %= 3600
    minuty = cas // 60
    sekundy = cas % 60

    return dny, hodiny, minuty, sekundy

if __name__ == "__main__":
    cas_v_sekundach = int(input("Zadejte čas v sekundách: "))
    dny, hodiny, minuty, sekundy = prevod_sekund(cas_v_sekundach)
    print(f"{dny} dní, {hodiny} hodin, {minuty} minut, {sekundy} sekund")
