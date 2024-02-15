def morseovka():
    morse_abeceda = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
    
    text = input("Zadejte text (maximálně 5 písmen): ").upper()

    morse = ""
    for znak in text:
        if znak in morse_abeceda:
            morse += morse_abeceda[znak] + " "
        else:
            morse += "/ "
    return morse.strip()

if __name__ == "__main__":
    print("Morseova abeceda:", morseovka())
