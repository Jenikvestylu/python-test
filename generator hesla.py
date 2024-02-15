import random
import string

def generuj_heslo(delka=10):
    znaky = string.ascii_letters + string.digits
    return ''.join(random.choice(znaky) for _ in range(delka))

if __name__ == "__main__":
    delka_hesla = int(input("Zadejte délku hesla: "))
    print("Generované heslo:", generuj_heslo(delka_hesla))
