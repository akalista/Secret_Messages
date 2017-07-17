class Cipher:

    ''' Cipher class is parent to all other classes, contains original encryp and decrypt along with the padding
    functions. Padding functions add the ability to give a one time pad while encrypting and decrypting to
    further help secure the message. On the encryption side it also limits the output to 5 chars at a time, for ex
    XXXXX CCCCC VVVVV ect... The new pad function creates an extended pad to cover the length of the message, and the
    has numbers function checks to see if the pad contains any digits. Padding encrypt/decrypt functions add or
    subtract the one time pad from the message.
    '''

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    #  Creates new pad if pad is smaller than the message given
    @staticmethod
    def new_pad(pad, message):

        if len(message) / len(pad) == 1:
            pad = pad
            return pad
        else:
            if len(message) % len(pad) == 0:
                diff1 = len(message) / len(pad)
                pad = pad * int(diff1)
                return pad
            elif len(message) % len(pad) != 0:
                diff2 = len(message) % len(pad)
                len_diff = len(message) - diff2
                div_diff = len_diff / len(pad)
                pad = (pad * int(div_diff)) + pad[:diff2]
                return pad

    #  Checks if pad has any numbers
    @staticmethod
    def has_numbers(pad):
        return any(char.isdigit() for char in pad)

    #  Padding encryption
    def padding_encrypt(self, message):
        #  Set alphabet list, get message length
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        message_length = len(message)

        #  While loop to protect for mistakes
        while True:
            #  Take in pad, check for correct pad length and see if it has any numbers
            pad = input("What would you like for the pad (must be <= the length of the message)?\n>>")
            if len(str(pad)) > message_length:
                print("The pad should be the same size or smaller than the message (for maximum security)!\n")
                continue
            if self.has_numbers(pad):
                print("The pad cant contain numbers!\n")
                continue

            #  Make pad into list
            pad1 = list(pad.upper())
            #  Add ords to list
            message_ord = [ord(x) for x in pad1]
            #  Subtract 65 from ords to correct for alphabet
            message_ord1 = [(x - 65) for x in message_ord]
            # Create new pad if necessary
            message_ord1 = (self.new_pad(message_ord1, message))
            #  Get ords - 65 for alphabet indexes
            user_ord = [ord(x) - 65 for x in message]
            #  Add  indexes and % 26 for new letters
            word_ord = [(x + y) % 26 for x, y in zip(message_ord1, user_ord)]
            #  Create new word list
            string_word = [alphabet[x] for x in word_ord]

            # Create final word list 5 chars at a time and join into string
            final_word = [x for y in (string_word[i:i+5] + [" "] * (i < len(string_word) - 4) for
                          i in range(0, len(string_word), 5)) for x in y]
            return ''.join(final_word)

    #  Padding decryption
    def padding_decrypt(self, message):
        #  Set alphabet list, take out spaces from user message, and get len of message
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        message = list(message.upper().replace(" ", ""))
        message_length = len(message)

        #  While loop to protect for mistakes
        while True:
            #  Take in pad, check for correct pad length and see if it has any numbers
            pad = input("What was the pad (must be <= the length of the message)?\n>>")
            if len(str(pad)) > message_length:
                print("The pad should be the same size or smaller than the message (for maximum security)!\n")
                continue
            if self.has_numbers(pad):
                print("The pad cant contain numbers!\n")
                continue

            # Make pad into list
            pad1 = list(pad.upper())
            #  Add ords in message
            message_ord = [ord(x) for x in message]
            #  Add ords - 65 to correct for alphabet
            message_ord1 = [x - 65 for x in message_ord]
            #  Add ords - 65 for pad
            pad_ord = [ord(x) - 65 for x in pad1]
            #  Create new pad based on message
            pad_ord = (self.new_pad(pad_ord, message))
            #  Add  indexes and % 26 for new letters
            word_ord = [(x - y) % 26 for x, y in zip(message_ord1, pad_ord)]

            #  Get new word indexes and join into string
            string_word = [alphabet[x] for x in word_ord]
            return ''.join(string_word)
