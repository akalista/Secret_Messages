#  Import Cipher class
from Cipher import Cipher


class Affine(Cipher):

    ''' Affine Cipher class, formula for encryption uses two keys and the index of the current alhabet letter
    to form a new index for the message. Formula is (a*x + b) % 26, where "a" is key1 (which is a coprime of 26),
    and "b" is key2 which is anything from 0-25. Decryption follow the formula a^-1(x-b) % 26, where a^-1 is
    the modular multiplicative inverse of a % m and b is key 2 from the encryption.

    This class includes and __init__that sets the alphabet, an encryption and decryption function to use the above
    formula, an in range function to check for user input validity, and two function to find the modular multiplicative
    inverse. Along with those are the actual encryption and decryption functions.
    '''

    #  __init__ defines the English alphabet
    def __init__(self):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Static method to find the encryption index
    @staticmethod
    def __affine_encrypt(eq_1, eq_2, num):
        return (eq_1*num + eq_2) % 26

    # Static method to find the decryption index
    @staticmethod
    def __affine_decrypt(eq_1, eq_2, num):
        return (eq_1*(num - eq_2)) % 26

    #  Static method to check the range of "a"
    @staticmethod
    def __in_range(num):
        return True if num in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25] else False

    #  Static method to find the gcd between two numbers, used in __mod_inv
    @staticmethod
    def __extended_gcd(aa, bb):
        #  Swap abs values and then 0, 1 's
        last_rem, rem = abs(aa), abs(bb)
        x, last_x, y, last_y = 0, 1, 1, 0
        #  While loop to return last_rem, last_x, and last_y
        while rem:
            last_rem, (quotient, rem) = rem, divmod(last_rem, rem)
            x, last_x = last_x - quotient * x, x
            y, last_y = last_y - quotient * y, y
        return last_rem, last_x * (-1 if aa < 0 else 1), last_y * (-1 if bb < 0 else 1)

    #  Mod_inv function for decryption
    def __mod_inv(self, a, m):
        #  Call __extended_gcd
        g, x, y = self.__extended_gcd(a, m)
        if g != 1:
            raise ValueError
        #  Return x mod m
        return x % m

    #  Encryption function
    def encrypt(self):
        #  Make user input into a list of uppercase chars, take out spaces, add padding
        user_input = input("What is the message to encode?\n>> ").upper().replace(" ", "")
        user_input = self.padding_encrypt(list(user_input))

        #  While loop to check for mistakes
        while True:
            #  Key1 input, check for digits and correct range, restart loop if incorrect
            key1 = input("Input key \"a\"(Must be coprime with 26) \n>>")
            if not key1.isdigit():
                print("That key wont work, try one of these! \"1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25\"\n")
                continue
            if not self.__in_range(int(key1)):
                print("That key wont work, try one of these! \"1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25\"\n")
                continue

            #  Key2 input, check for digits and correct range, restart loop if incorrect
            key2 = input("Input key \"b\" (Integers up to 25) \n>>")
            if not key2.isdigit():
                print("Key 2 must be between 0 and 25!\n")
                continue
            if int(key2) not in range(26):
                print("Key 2 must be between 0 and 25!\n")
                continue

            #  Turn keys into int
            key1 = int(key1); key2 = int(key2)

            #  Turn spaces into spaces and the rest into the int ords - 65 to correct for alphabet
            new_ords1 = [" " if x == " " else (int(ord(x) - 65)) for x in user_input]

            #  Turn spaces into spaces, rest goes through the encryption formula
            new_ords2 = [" " if x == " " else (self.__affine_encrypt(key1, key2, x)) for x in new_ords1]

            #  Turn spaces into spaces, rest are turned into letters using alphabet
            encrypted = [" " if x == " " else (self.alphabet[x]) for x in new_ords2]

            #  Return final message
            return "Your message after encoding is " + ''.join(encrypted) + "!\n"

    #  Decryption function
    def decrypt(self):
        #  Make user_input into a list of uppercase chars
        user_input = list(input("What is the message to decode?\n>> ").upper())

        #  While loop to check for mistakes
        while True:
            #  Key1 input, check for digits and correct range, restart loop if incorrect
            key1 = input("Input key \"a\"(Must be coprime with 26) \n>>")
            if not key1.isdigit():
                print("That key wont work, try one of these! \"1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25\"\n")
                continue
            if not self.__in_range(int(key1)):
                print("That key wont work, try one of these! \"1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25\"\n")
                continue

            # Key2 input, check for digits and correct range, restart loop if incorrect
            key2 = input("Input key \"b\"(Number between 0 and 25) \n>>")
            if not key2.isdigit():
                print("Key 2 must be between 0 and 25!\n")
                continue
            if int(key2) not in range(26):
                print("Key 2 must be between 0 and 25!\n")
                continue

            #  Turn keys into ints, use key1 and alphabet length to create modular multiplicative inverse
            key1 = int(key1); key2 = int(key2)
            mod_inv = self.__mod_inv(key1, 26)

            #  Turn spaces into spaces, rest is ord - 65 to give alphabet index
            new_ords1 = [" " if x == " " else (ord(x) - 65) for x in user_input]

            #  Turn spaces into spaces, rest goes into the decryption formula to find new ords
            new_ord2 = [" " if x == " " else (self.__affine_decrypt(mod_inv, key2, int(x))) for x in new_ords1]

            #  Turn spaces into spaces, rest turn into letters using alphabet
            decrypted = [" " if x == " " else (self.alphabet[x]) for x in new_ord2]

            #  Join list into a string
            decrypted1 = ''.join(decrypted)

            #  Add padding to the string using padding_decrypt in Cipher class
            decrypted1 = self.padding_decrypt(decrypted1)

            #  Return final message
            return "Your code after description is " + decrypted1 + "!\n"
