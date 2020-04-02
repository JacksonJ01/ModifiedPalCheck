# Jackson Jared
# 3.31.2020
from time import sleep
from getpass import getuser


# This function checks if the string the user entered is a palindrome
def palindrome_check(check):
    check = check.lower().replace(' ', '')
    length = int(len(check))
    if length == 0 or length == 1:
        print("True")
        return True
    elif check[0] != check[-1]:
        print("False")
        return False
    else:
        palindrome_check(check[1:-1])


input("PRESS ENTER")

name = input("\nHello there user, what is your name?"
             "\n>>>").title()

print(f"""{name}, do you know what a palindrome is?
Basically it is when a word of phrase is spelled the same forward and backwards..
Watch, I'll show you.""")

# Demonstrates what the program will do
demonstrate = 0
while demonstrate != 'radar':
    demonstrate = input("Type the word radar"
                        "\n>>>").lower()
    if demonstrate == "radar":
        print(palindrome_check(demonstrate))

sleep(1)
print("\nDo you see how I returned True?(Don't worry about the None... kinks in the system)"
      f"\nI, {getuser()}, have a program that allows you to enter a words and see if they are indeed a palindrome"
      f"\nOkay {name}, I'm going to let you have your fun now, but first:"
      "\nIf you want to continue and enter more text type C or 1"
      "\nIf you want to leave type L or 2")

string = "Empty"
while string != 0:
    sleep(1.5)
    cont = input("\nWhat do you want to do?"
                 "\n1. Continue"
                 "\n2. Leave"
                 "\n>>>").title()
    if cont == '1' or cont == "C":
        string = input("\nEnter a string please"
                       "\nNo punctuation needed"
                       "\n>>>")
        # calls the function, entering the input statement as a parameter
        print(palindrome_check(string))
    elif cont == '2' or cont == 'L':
        print("Have a good day", name)
        string = 0
