import re

def validace_hesla(heslo):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', heslo))

if __name__ == "__main__":
    heslo = input("Zadejte heslo pro validaci: ")
    if validace_hesla(heslo):
        print("Heslo je platné.")
    else:
        print("Heslo není platné.")
