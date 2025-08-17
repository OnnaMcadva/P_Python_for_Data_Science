import sys

NESTED_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/"
}


def encode_morse(text):
    """
    Encode a string into Morse code using NESTED_MORSE dictionary.
    Raises AssertionError if text contains invalid characters.
    """
    text = text.upper()
    morse_list = []
    for char in text:
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        morse_list.append(NESTED_MORSE[char])
    return " ".join(morse_list)


def main():
    """
    Main function to handle command line arguments and output Morse code.
    """
    try:
        if len(sys.argv) != 2 or not isinstance(sys.argv[1], str):
            raise AssertionError("the arguments are bad")
        text = sys.argv[1]
        result = encode_morse(text)
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
