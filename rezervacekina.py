def rezervace_sedadla(kino, radek, sedadlo):
    if kino[radek][sedadlo] == 'X':
        return "Sedadlo je již obsazeno."
    else:
        kino[radek][sedadlo] = 'X'
        return "Sedadlo úspěšně zarezervováno."

if __name__ == "__main__":
    kino = [
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O']
    ]

    radek = int(input("Zadejte řádek sedadla (1-4): ")) - 1
    sedadlo = int(input("Zadejte sedadlo (1-5): ")) - 1

    print(rezervace_sedadla(kino, radek, sedadlo))
