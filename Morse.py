# import time

Morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..'}


def convert_single(letter):
    letter = str(letter).upper()
    if len(letter) > 1 and ('.' not in letter and '-' not in letter):
        print("Not a single char!  Converting...")
        letter = letter[0:1]
    if letter in Morse:
        return Morse[letter]
    elif letter in Morse.values():
        return list(Morse.keys())[list(Morse.values()).index(letter)]
    else:
        print("Unable to match!")
        return ''


def convert_all(string):
    string = str(string).upper()
    # conversion = []
    converted = ""
    for c in string:
        if c == ' ':
            converted = converted + '   '

        elif c in Morse:
            #Only reads one letter at a time (fix that)
            converted = converted + Morse.get(c) + " "
        elif c in Morse.values():  # if a code char
            converted = converted + list(Morse.keys())[list(Morse.values()).index(c)]
        else:
            converted = converted + "(?) "
    return converted


# print('\n'+convert_single(input("Please enter a character to convert: ")))
print('\n\n\n'+convert_all(input("Enter a phrase to convert: ")))
