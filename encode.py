import random
import re

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]

values = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]

key = {}

def generate_key():
    random.shuffle(values)
    index = 0
    crypto_top = "| "
    crypto_bottom = "| "
    for letter in alphabet:
        crypto_top += f"{letter} | "
        crypto_bottom += f"{values[index]} | "
        key[letter] = values[index]
        index += 1

    print(crypto_top)
    print(crypto_bottom)
    print("\n")

def encode_string(phrase):
    generate_key()

    new_phrase = ""
    upper_phrase = phrase.upper()
    for letter in upper_phrase:
        encoded_letter = letter

        # Make sure it's a letter
        if re.search('[A-Z]', letter):
            # If it's not a space, number, or punctuation
            encoded_letter = key[letter]

        new_phrase += encoded_letter

    print("\nEncoded Phrase:")
    print(upper_phrase)
    print(new_phrase)

# encode_string("Python is #1!! Don't  you agree?")
encode_string('"Cats are the best animal ever!" - Josie Swertfeger, Oct. 6, 2023')
