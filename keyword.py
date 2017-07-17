#  Import Cipher class
from Cipher import Cipher


class Keyword(Cipher):

    ''' Keyword cipher takes in a keyword given by the user and adjusts the alphabet using it. For
    example, if the keyword was "hey", the alphabet would start out with heyabcd ect.. however, the chars in
    "hey" would be taken out of that alphabet. If the keyword contains duplicate letters they are taken out.
    For example, "hello" would start the alphabet as heloabc ect.. The new alphabet is used to encode and
    decode messages.

    This class contains an __init__  that sets the alphabet, a check function to take out duplicate letters in a
    a string, a new alphabet function to create a new alphabet according to the keyword, and the encrypt
    and decrypt functions.
    '''

    #  __init__ defines the alphabet
    def __init__(self):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    #  Checks for multiples of any letter and takes it out
    @staticmethod
    def __check(seq):
        checked = []
        for e in seq:
            if e not in checked:
                checked.append(e)
        return checked

    #  Creates new alphabet using keyword given by user
    def __new_alphabet(self, user_key):
        for k in user_key:
            if k in self.alphabet:
                self.alphabet.remove(k)

        output = (user_key + self.alphabet)
        return output

    #  Encryption function
    def encrypt(self):
        #  User input made into a list of uppercase chars, take out spaces, add padding
        user_input = input("What is the message to encode?\n>> ").upper().replace(" ", "")
        user_input = self.padding_encrypt(list(user_input))
        #  Key made into uppercase list
        key = list(input("What would you like to use as the key?\n>> ").upper())

        #  Check key and set new alphabet
        key1 = self.__check(key)
        final_alphabet = self.__new_alphabet(key1)

        #  Create list of ords - 65 for alphabet indexes
        list1 = [(ord(x) - 65) for x in user_input]
        #  Add space if space otherwise the letter of the alphabet
        list2 = [(" " if x < 0 else (final_alphabet[x])) for x in list1]

        #  Return message
        return "Your message after encoding is " + ''.join(list2) + "!\n"

    #  Decryption function
    def decrypt(self):
        #  Turn message and key into uppercase list, reset alphabet
        user_input = list(input("What is the message to decode?\n>> ").upper())
        key0 = list(input("What is the key?\n>> ").upper())
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        #  Check key and set new alphabet
        key1 = self.__check(key0)
        final = self.__new_alphabet(key1)

        #  Add space if space otherwise add index of letter given
        list_ord = [(final.index(x) if x in final else " ") for x in user_input]
        #  Add space if space otherwise add letter from alphabet
        final_word = [(" " if x == " " else (alphabet[x])) for x in list_ord]
        #  Join list and add padding
        final_word1 = ''.join(final_word)
        final_word1 = self.padding_decrypt(final_word1)

        #  Return message
        return "Your message after decoding is " + final_word1 + "!\n"
