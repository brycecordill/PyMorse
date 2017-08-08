Morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..'}


def convert_single(letter):
    # Force upper case
    letter = str(letter).upper()
    # Checks if a single letter or in Morse code
    if len(letter) > 1 and ('.' not in letter and '-' not in letter):
        print("Not a single char!  Converting...")
        # Reduces to single character if not in Morse
        letter = letter[0:1]
    if letter in Morse:  # if it's a letter
        return Morse[letter]
    elif letter in Morse.values():  # if it's morse
        return list(Morse.keys())[list(Morse.values()).index(letter)]
    else:
        print("Unable to match!")
        return ''


# Checks whether string is Morse or text, then sends to correct f()
def check_morse(string):
    string = str(string).upper()
    mCode = True  # True if in Morse, false if it's text

    for ch in list(string):
        # mCode is false if there are any characters except dots or dashes
        if not(ch is '.' or ch is '-' or ch is ' '):
            mCode = False
    if mCode:
        return convert_to_text(string)
    else:
        return convert_to_morse(string)


def convert_to_morse(string):
    converted = ""
    for ch in list(string):
        # Checks if the character can be converted
        if ch in Morse:
            converted += Morse.get(ch) + " "
        # Turns spaces into 3 spaces to separate words
        elif ch == " ":
            converted += "   "
        # If character cannot be converted
        else:
            converted += "(?)"
    return converted


def convert_to_text(string):
    converted = ""
    # Counts number of spaces to determine if it's a new word; reset on - or .
    spaceCount = 0
    # Way to find spaces after split
    string = string.replace(' ', ' ^ ').split()
    for word in string:
        # If it's a space
        if word == '^':
            if spaceCount < 2:
                spaceCount += 1
            # Adds a space in converted for a new word
            else:
                converted += " "
                spaceCount = 0
        elif word in Morse.values():
            spaceCount = 0
            # Adds letter to converted
            converted += list(Morse.keys())[list(Morse.values()).index(word)]
        else:
            # If it cannot be converted
            converted += "(?)"
    return converted


print(check_morse(input("Enter a phrase to convert: ")))

