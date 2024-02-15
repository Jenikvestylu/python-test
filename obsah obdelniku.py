def obsah_obdelnika(a, b):
    return a * b

if __name__ == "__main__":
    a = float(input("Zadejte délku strany a: "))
    b = float(input("Zadejte délku strany b: "))
    print("Obsah obdélníka:", obsah_obdelnika(a, b))
