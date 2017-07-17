# Import OS and other Cipher classes
import os
from keyword import Keyword
from atbash import Atbash
from affine import Affine


# Clear Screen for Shell
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main function to run application
def main():

    ''' Main(), has available ciphers and runs a while loop to correct for errors.
    Asks for one of the ciphers and runs cipher classes based on the answers.
    Second while loop corrects for Encryption/Decryption input. After cipher classes run
    in second loop, user is asked if he/she would like to play through the loop again.
    '''

    #  First while loop and available cipher list
    available = ["keyword", "atbash", "affine"]
    run = True

    while run:
        play = True
        #  Prints "Main Menu" and asks for choice of cipher
        print("Welcome to the secret messages program!\n\nHere are the available ciphers: ")
        print("-Keyword\n-Atbash\n-Affine")
        print("Select a cipher or type \"QUIT\" before the program starts to exit!\n")
        user_input = input("What cipher would you like to use?\n>> ")

        if user_input.upper() == "QUIT":
            print("\nGoodbye!")
            break

        #  Checks user input for validity
        if user_input.lower() in available:
            play = True
        elif user_input.lower() not in available:
            print("That's not an option!\n")
            clear_screen()
            # print('\n' * 80) = Pseudo clear_screen() for Py Charm, ONLY FOR USE ON PYCHARM
            continue

        while play:
            #  3 part for loop to run cipher encode/decode based on user input choice
            if user_input.lower() == "keyword":
                #  Keyword class start
                play_game = Keyword()
                answer = input("Would you like to (E)ncrypt or (D)ecrypt?\n>> ")
                #  Check for validity answer
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
                #  Atbash class start
                play_game = Atbash()
                answer = input("Would you like to (E)ncrypt or (D)ecrypt?\n>> ")
                #  Check for validity answer
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
                #  Affine class start
                play_game = Affine()
                answer = input("Would you like to (E)ncrypt or (D)ecrypt?\n>> ")
                #  Check for validity answer
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

            #  Ask user to play again, if yes clear and play again, else close both loops
            play = input("Would you like to play again (Y or N)?\n>> ")
            if play.upper() == "Y":
                clear_screen()
                break
            elif play.upper() == "N":
                print("Hope you had a good time!")
                play = False
                run = False

        continue

#  Run main() function
main()
