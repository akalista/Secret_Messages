#  All imports
import os
from keyword import Keyword
from atbash import Atbash
from affine import Affine


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    available = ["keyword", "atbash", "affine"]
    run = True

    while run:
        play = True
        print("Welcome to the secret messages program!\n\nHere are the available ciphers: ")
        print("-Keyword\n-Atbash\n-Affine")
        print("Select a cipher or type \"QUIT\" before the program starts to exit!\n")
        user_input = input("What cipher would you like to use?\n>> ")

        if user_input.upper() == "QUIT":
            print("\nGoodbye!")
            break

        if user_input.lower() in available:
            play = True
        elif user_input.lower() not in available:
            print("That's not an option!\n")
            clear_screen()
            # print('\n' * 80) = Pseudo clear_screen() for Py Charm, ONLY FOR USE ON PYCHARM
            continue

        while play:
            if user_input.lower() == "keyword":
                play_game = Keyword()
                answer = input("Would you like to (E)ncrypt or (D)ecrypt?\n>> ")
                if answer.upper() == "E":
                    print(play_game.encrypt())
                elif answer.upper() == "D":
                    print(play_game.decrypt())
                elif answer.upper() == "QUIT":
                    print("\nGoodbye!")
                    run = False
                    break
                else:
                    print("Wrong input! Try \"E\" or \"D\"!\n")
                    continue
            elif user_input.lower() == "atbash":
                play_game = Atbash()
                answer = input("Would you like to (E)ncrypt or (D)ecrypt?\n>> ")
                if answer.upper() == "E":
                    print(play_game.encrypt())
                elif answer.upper() == "D":
                    print(play_game.decrypt())
                elif answer.upper() == "QUIT":
                    print("\nGoodbye!")
                    run = False
                    break
                else:
                    print("Wrong input! Try \"E\" or \"D\"!\n")
                    continue
            elif user_input.lower() == "affine":
                play_game = Affine()
                answer = input("Would you like to (E)ncrypt or (D)ecrypt?\n>> ")
                if answer.upper() == "E":
                    print(play_game.encrypt())
                elif answer.upper() == "D":
                    print(play_game.decrypt())
                elif answer.upper() == "QUIT":
                    print("\nGoodbye!")
                    run = False
                    break
                else:
                    print("Wrong input! Try \"E\" or \"D\"!\n")
                    continue

            play = input("Would you like to play again (Y or N)?\n>> ")
            if play.upper() == "Y":
                clear_screen()
                break
            elif play.upper() == "N":
                print("Hope you had a good time!")
                play = False
                run = False

        continue

main()
