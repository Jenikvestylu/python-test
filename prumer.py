def prumer(seznam):
    return sum(seznam) / len(seznam)

if __name__ == "__main__":
    seznam_cisel = [1, 2, 3, 4, 5]
    print("Průměr:", prumer(seznam_cisel))
