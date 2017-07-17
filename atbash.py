#  Import Cipher class
from Cipher import Cipher


class Atbash(Cipher):

    '''
    Atbash cipher class uses the alphabet in reverse to encrypt and decrypt messages.

    This class contains an __init__ that sets an alphabet in reverse along with the
    encryption and decryption functions.
    '''

    #  __init__ defines the English alphabet in reverse
    def __init__(self):
        self.alphabet = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

    #  Encryption function
    def encrypt(self):
        #  User input made into a list of uppercase chars, take out spaces, add padding
        user_input = input("What is the message to encode?\n>> ").upper().replace(" ", "")
        user_input = self.padding_encrypt(list(user_input))

        #  Turns spaces into spaces and the rest into ords -65 to correct for alphabet index
        ord_list = [(" " if x == " " else (ord(x) - 65)) for x in user_input]
        #  Turn spaces into spaces and the rest into an alphabet index
        final_list = [(" " if x == " " else (self.alphabet[x])) for x in ord_list]

        #  Return final message
        return "Your message after encoding is " + ''.join(final_list) + "!\n"

    #  Decryption function
    def decrypt(self):
        #  User input made into a list of uppercase chars
        user_input = list(input("What is the message to decode?\n>> ").upper())

        #  Turn spaces into spaces and the rest into indexes of the alphabet
        ord_list = [(" " if x == " " else (self.alphabet.index(x))) for x in user_input]
        #  Turn spaces into spaces and rest back to chars from ords using + 65 to adjust from alphabet
        final_list = [(" " if x == " " else (chr(x + 65))) for x in ord_list]
        #  Join fina list and apply padding
        final_list1 = ''.join(final_list)
        final_list1 = self.padding_decrypt(final_list1)

        #  Return final message
        return "Your message after decoding is " + final_list1 + "!\n"



