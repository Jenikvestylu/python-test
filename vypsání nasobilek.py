def vypis_nasobilky(rozsah):
    for i in range(1, rozsah+1):
        for j in range(1, rozsah+1):
            print(f"{i} * {j} = {i*j}")
        print()

if __name__ == "__main__":
    rozsah = int(input("Zadejte rozsah násobilky: "))
    vypis_nasobilky(rozsah)
