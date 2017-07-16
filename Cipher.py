class Cipher:

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

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

    @staticmethod
    def has_numbers(pad):
        return any(char.isdigit() for char in pad)

    def padding_encrypt(self, message):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        message = list(message.upper().replace(" ", ""))
        message_length = len(message)

        while True:
            pad = input("What would you like for the pad (must be <= the length of the message)?\n>>")
            if len(str(pad)) > message_length:
                print("The pad should be the same size or smaller than the message (for maximum security)!\n")
                continue
            if self.has_numbers(pad):
                print("The pad cant contain numbers!\n")
                continue

            pad1 = list(pad.upper())

            message_ord = [ord(x) for x in pad1]
            message_ord1 = [(x - 65) for x in message_ord]
            message_ord1 = (self.new_pad(message_ord1, message))
            user_ord = [ord(x) - 65 for x in message]
            word_ord = [(x + y) % 26 for x, y in zip(message_ord1, user_ord)]
            string_word = [alphabet[x] for x in word_ord]

            final_word = [x for y in (string_word[i:i+5] + [" "] * (i < len(string_word) - 4) for
                          i in range(0, len(string_word), 5)) for x in y]
            return ''.join(final_word)

    def padding_decrypt(self, message):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        message = list(message.upper().replace(" ", ""))
        message_length = len(message)

        while True:
            pad = input("What was the pad (must be <= the length of the message)?\n>>")
            if len(str(pad)) > message_length:
                print("The pad should be the same size or smaller than the message (for maximum security)!\n")
                continue
            if self.has_numbers(pad):
                print("The pad cant contain numbers!\n")
                continue

            pad1 = list(pad.upper())
            message_ord = [ord(x) for x in message]
            message_ord1 = [x - 65 for x in message_ord]
            pad_ord = [ord(x) - 65 for x in pad1]
            pad_ord = (self.new_pad(pad_ord, message))
            word_ord = [(x - y) % 26 for x, y in zip(message_ord1, pad_ord)]
            string_word = [alphabet[x] for x in word_ord]

            return ''.join(string_word)

