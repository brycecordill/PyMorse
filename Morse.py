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
    if letter in Morse:  # if it's a letter
        return Morse[letter]
    elif letter in Morse.values():  # if it's morse
        return list(Morse.keys())[list(Morse.values()).index(letter)]
    else:
        print("Unable to match!")
        return ''


def check_morse(string):
    string = str(string).upper()
    mCode = True

    for ch in list(string):
        # checks if in morse code, false if not
        if not(ch is '.' or ch is '-' or ch is ' '):
            mCode = False
    if mCode:
        return convert_to_text(string)
    else:
        return convert_to_morse(string)


def convert_to_morse(string):
    converted = ""
    for ch in list(string):
        if ch in Morse:
            converted += Morse.get(ch) + " "
        elif ch == " ":
            converted += "   "
        else:
            converted += "(?)"
    return converted


def convert_to_text(string):
    converted = ""
    spaceCount = 0
    # way to find spaces after split
    string = string.replace(' ', ' ^ ').split()
    for word in string:
        if word == '^':
            if spaceCount < 2:
                spaceCount += 1
            else:
                converted += " "
                spaceCount = 0
        else:
            spaceCount = 0
            converted += list(Morse.keys())[list(Morse.values()).index(word)]
    return converted


# print('\n'+convert_single(input("Please enter a character to convert: ")))
print('\n\n\n'+check_morse(input("Enter a phrase to convert: ")))
