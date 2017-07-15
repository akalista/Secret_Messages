from Cipher import Cipher


class Atbash(Cipher):

    def __init__(self):
        self.alphabet = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

    def encrypt(self):
        constant = 65
        user_input = list(input("What is the message to encode?\n>> ").upper())

        ord_list = [(" " if x == " " else (ord(x) - constant)) for x in user_input]
        final_list = [(" " if x == " " else (self.alphabet[x])) for x in ord_list]

        return "Your message after encoding is " + ''.join(final_list) + "!\n"

    def decrypt(self):
        constant = 65
        user_input = list(input("What is the message to decode?\n>> ").upper())

        ord_list = [(" " if x == " " else (self.alphabet.index(x))) for x in user_input]
        final_list = [(" " if x == " " else (chr(x + constant))) for x in ord_list]

        return "Your message after decoding is " + ''.join(final_list) + "!\n"



