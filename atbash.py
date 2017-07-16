from Cipher import Cipher


class Atbash(Cipher):

    def __init__(self):
        self.alphabet = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

    def encrypt(self):
        constant = 65
        user_input = list(input("What is the message to encode?\n>> ").upper())

        ord_list = [(" " if x == " " else (ord(x) - constant)) for x in user_input]
        final_list = [(" " if x == " " else (self.alphabet[x])) for x in ord_list]
        final_list1 = ''.join(final_list)
        final_list1 = self.padding_encrypt(final_list1)

        return "Your message after encoding is " + final_list1 + "!\n"

    def decrypt(self):
        constant = 65
        user_input = list(input("What is the message to decode?\n>> ").upper())

        ord_list = [(" " if x == " " else (self.alphabet.index(x))) for x in user_input]
        final_list = [(" " if x == " " else (chr(x + constant))) for x in ord_list]
        final_list1 = ''.join(final_list)
        final_list1 = self.padding_decrypt(final_list1)

        return "Your message after decoding is " + final_list1 + "!\n"



