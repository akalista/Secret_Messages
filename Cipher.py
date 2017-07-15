class Cipher:
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    def padding(self, message):
        message = list(message.upper())

        while True:
            pad = input("What would you like for the pad (same length string as the message)?\n>>")
            if len(str(pad)) != len(message):
                print("Message and pad should be the same length (for maximum security)!\n")
                continue
            if pad.index(" ") != message.index(" "):
                print("Message and pad should be the same length (for maximum security)!\n")
                continue

            pad1 = list(pad.upper())

            message_ord = [ord(x) for x in pad1]
            message_ord1 = [(x - 65) for x in message_ord]
            message_ord2 = [(ord(x) - 65) for x in message]
            combined = [x + y for x, y in zip(message_ord1, message_ord2)]
            word = [" " if x < 0 else (self.alphabet[x]) for x in combined]

            print(word)
            final_word = []
            for x in word:
                if len(word) >= 5:
                    final_word.append()
                else:
                    final_word.append(x)

            print(final_word)
            break


test = Cipher()
test.padding("He llo")
