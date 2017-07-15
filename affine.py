from Cipher import Cipher

class Affine(Cipher):
    def __init__(self):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    @staticmethod
    def __affine_encrypt(eq_1, eq_2, num):
        return (eq_1*num + eq_2) % 26

    @staticmethod
    def __affine_decrypt(eq_1, eq_2, num):
        return (eq_1*(num - eq_2)) % 26

    @staticmethod
    def __in_range(num):
        return True if num in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25] else False

    @staticmethod
    def __extended_gcd(aa, bb):
        last_rem, rem = abs(aa), abs(bb)
        x, last_x, y, last_y = 0, 1, 1, 0
        while rem:
            last_rem, (quotient, rem) = rem, divmod(last_rem, rem)
            x, last_x = last_x - quotient * x, x
            y, last_y = last_y - quotient * y, y
        return last_rem, last_x * (-1 if aa < 0 else 1), last_y * (-1 if bb < 0 else 1)

    def __mod_inv(self, a, m):
        g, x, y = self.__extended_gcd(a, m)
        if g != 1:
            raise ValueError
        return x % m

    def encrypt(self):
        user_input = list(input("What is the message to encode?\n>> ").upper())

        while True:
            key1 = input("Input key \"a\"(Must be coprime with 26) \n>>")
            if not key1.isdigit():
                print("That key wont work, try one of these! \"1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25\"\n")
                continue
            if not self.__in_range(int(key1)):
                print("That key wont work, try one of these! \"1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25\"\n")
                continue

            key2 = input("Input key \"b\" (Integers up to 25) \n>>")
            if not key2.isdigit():
                print("Key 2 must be between 0 and 25!\n")
                continue
            if int(key2) not in range(26):
                print("Key 2 must be between 0 and 25!\n")
                continue

            key1 = int(key1); key2 = int(key2)

            new_ords1 = [" " if x == " " else (int(ord(x) - 65)) for x in user_input]
            new_ords2 = [" " if x == " " else (self.__affine_encrypt(key1, key2, x)) for x in new_ords1]
            encrypted = [" " if x == " " else (self.alphabet[x]) for x in new_ords2]

            return "Your message after encoding is " + ''.join(encrypted) + "!\n"

    def decrypt(self):
        user_input = list(input("What is the message to decode?\n>> ").upper())

        while True:
            key1 = input("Input key \"a\"(Must be coprime with 26) \n>>")
            if not key1.isdigit():
                print("That key wont work, try one of these! \"1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25\"\n")
                continue
            if not self.__in_range(int(key1)):
                print("That key wont work, try one of these! \"1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25\"\n")
                continue

            key2 = input("Input key \"b\"(Number between 0 and 25) \n>>")
            if not key2.isdigit():
                print("Key 2 must be between 0 and 25!\n")
                continue
            if int(key2) not in range(26):
                print("Key 2 must be between 0 and 25!\n")
                continue

            key1 = int(key1); key2 = int(key2)
            mod_inv = self.__mod_inv(key1, 26)

            new_ords1 = [" " if x == " " else (ord(x) - 65) for x in user_input]
            new_ord2 = [" " if x == " " else (self.__affine_decrypt(mod_inv, key2, int(x))) for x in new_ords1]
            decrypted = [" " if x == " " else (self.alphabet[x]) for x in new_ord2]

            return "Your code after description is " + ''.join(decrypted) + "!"
