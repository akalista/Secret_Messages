from Cipher import Cipher


class Keyword(Cipher):

    def __init__(self):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    @staticmethod
    def check(seq):
        checked = []
        for e in seq:
            if e not in checked:
                checked.append(e)
        return checked

    def new_alphabet(self, user_key):
        for k in user_key:
            if k in self.alphabet:
                self.alphabet.remove(k)

        output = (user_key + self.alphabet)
        return output

    def encrypt(self):
        user_input = list(input("What is the message to encode?\n>> ").upper())
        key = list(input("What would you like to use as the key?\n>> ").upper())

        key1 = self.check(key)
        final_alphabet = self.new_alphabet(key1)

        list1 = [(ord(x) - 65) for x in user_input]
        list2 = [(" " if x < 0 else (final_alphabet[x])) for x in list1]
        list3 = ''.join(list2)
        list3 = self.padding_encrypt(list3)

        return "Your message after encoding is " + list3 + "!\n"

    def decrypt(self):
        user_input = list(input("What is the message to decode?\n>> ").upper())
        key0 = list(input("What is the key?\n>> ").upper())
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        key1 = self.check(key0)
        final = self.new_alphabet(key1)

        list_ord = [(final.index(x) if x in final else " ") for x in user_input]
        final_word = [(" " if x == " " else (alphabet[x])) for x in list_ord]
        final_word1 = ''.join(final_word)
        final_word1 = self.padding_decrypt(final_word1)

        return "Your message after decoding is " + final_word1 + "!\n"
