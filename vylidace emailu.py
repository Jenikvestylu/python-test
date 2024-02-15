import re

def validace_emailu(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

if __name__ == "__main__":
    email = input("Zadejte email pro validaci: ")
    if validace_emailu(email):
        print("Email je platný.")
    else:
        print("Email není platný.")
