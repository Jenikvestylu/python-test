def cenzura(text, vulgarni_slovo):
    return text.replace(vulgarni_slovo, '*' * len(vulgarni_slovo))

if __name__ == "__main__":
    text = input("Zadejte text, ve kterém chcete cenzurovat vulgární slovo: ")
    vulgarni_slovo = input("Zadejte vulgární slovo k cenzuře: ")
    print("Cenzurovaný text:", cenzura(text, vulgarni_slovo))
