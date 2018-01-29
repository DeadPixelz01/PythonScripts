# Imports.
import time
from termcolor import cprint, colored


# Defining functions
# Celsius to Fahrenheit.
def f_temp(x):
    return (x * 9/5) + 32


# Fahrenheit to Celsius.
def c_temp(x):
    return (x - 32) * 5 / 9


# Introduction message.
cprint("Fahrenheit to Celsius", 'blue')
cprint('---------------------', 'blue')
cprint('Description:', 'blue')
cprint('------------', 'blue')
cprint('Converts Fahrenheit to Celsius (or vice versa). \n', 'magenta')

# User input.
while True:
    usr_choice = input('Enter an operation (m for help): ')

    # Man page.
    if usr_choice == 'm':
        cprint('Man page', 'blue')
        cprint('--------', 'blue')
        cprint('1    converts Celsius to Fahrenheit', 'blue')
        cprint('2    converts Fahrenheit to Celsius', 'blue')
        cprint('3    stop and exits the script', 'blue')
        cprint('m    prints this man page \n', 'blue')
    
    # Converting Celsius to Fahrenheit.
    elif usr_choice == '1':
        celsius_input = int(input('Please enter the number you wish to convert to Fahrenheit: '))
        cprint("When '{old_temp}' is converted into Fahrenheit, we get '{new_temp}' \n"
               .format('green', old_temp=celsius_input, new_temp=f_temp(celsius_input)), 'green')

    # Converting Fahrenheit to Celsius.
    elif usr_choice == '2':
        fahrenheit_input = int(input('Please enter the number you wish to convert to Celsius: '))
        cprint("When '{old_temp}' is converted into Celsius, we get '{new_temp}' \n"
               .format(old_temp=fahrenheit_input, new_temp=c_temp(fahrenheit_input)), 'green')

    # Existing the script.
    elif usr_choice == '3':
        cprint('Exiting...', 'blue')
        cprint('Thank you for using FTC. If you enjoyed the script, support software like it =)', 'blue')
        cprint(' -Alex Smith', 'blue')
        time.sleep(1)
        quit()

    # Invalid input (user error).
    else:
        usr_error = colored("Invalid input! '{choice}' is not a valid operation. See man page for help."
                            .format(choice=usr_choice), 'red', attrs=['bold'])
        print(usr_error)
