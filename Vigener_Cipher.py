#! python 3.9
import pyperclip
"""
Chương trình mã hóa Vigenere

"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    myMessage = "Attack at dawn"
    myKey = "tuananh"
    myMode = "encrypt"

    if myMode == "encrypt":
        translated = encryptMessage(myKey, myMessage)
    elif myMode == "decrypt":
        translated = decryptMessage(myKey, myMessage)

    print("%sed message: " % myMode.title())
    print(translated)
    pyperclip.copy(translated)
    print("The message has been copied to the clipboard.")


def encryptMessage(key, message):
    return translateMessage(key, message, "encrypt")

def decryptMessage(key, message):
    return translateMessage(key, message, "decrypt")

def translateMessage(key, message, mode):
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        symIndex = alphabet.find(symbol.upper())
        if symIndex != -1:
            if mode == "encrypt":
                symIndex += alphabet.find(key[keyIndex])
            elif mode == "decrypt":
                symIndex -= alphabet.find(key[keyIndex])

            symIndex %= len(alphabet)
            if symbol.isupper():
                translated.append(alphabet[symIndex])
            elif symbol.islower():
                translated.append(alphabet[symIndex].lower())
            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)

    return "".join(translated)

if __name__ == '__main__':
    main()