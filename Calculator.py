# Imports
import sys
import time
from termcolor import colored, cprint


# Definitions for the four main mathematical operations.
def addition (x, y):
    return x + y

def subtraction (x, y):
    return x - y

def multiplication (x, y):
    return x * y

def division (x, y):
    return x / y


# Instructions and a guide on how to use the script.
cprint("Welcome to Alex's Python calculator!", 'blue')
cprint("Simply select a function and let APC do all the hard work. \n", 'blue')
cprint("1. Addition", 'green')
cprint("2. Subtraction", 'green')
cprint("3. Multiplication", 'green')
cprint("4. Division", 'green')


# Asks the user for input.
usr_choice = input("Pick a function (1/2/3/4): ")
cprint("Now enter that numbers you want to use in your equation.", 'blue')
number_1 = int(input("Number 1: "))
number_2 = int(input("Number 2: "))
print("\n")

# Prints the equation out for the user.
print("Here is your final equation...")
if usr_choice == '1':
   print(number_1,"+",number_2,"=", addition(number_1,number_2))

elif usr_choice == '2':
   print(number_1,"-",number_2,"=", subtraction(number_1,number_2))

elif usr_choice == '3':
   print(number_1,"*",number_2,"=", multiplication(number_1,number_2))

elif usr_choice == '4':
   print(number_1,"/",number_2,"=", division(number_1,number_2))
else:
# User error message.
   print("Invalid user input! Please run the script again and read over the instructions.")

